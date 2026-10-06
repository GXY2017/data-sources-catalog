# -*- coding: utf-8 -*-
"""Search portable public metadata; never contact a provider, account or local database."""
import argparse
import csv
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def load(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8'))

def matches(record, terms):
    text = json.dumps(record, ensure_ascii=False).casefold()
    return all(term.casefold() in text for term in terms)

def bundled_path(relative):
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(ROOT):
        raise ValueError('Catalog path must stay inside this repository')
    return path

def check(registry, index):
    errors = []
    sources = {s['id'] for s in registry['sources']}
    ids = [e['id'] for e in index['entries']]
    if len(ids) != len(set(ids)): errors.append('duplicate content IDs')
    if len(sources) != len(registry['sources']): errors.append('duplicate source IDs')
    profiles = {e['source_ids'][0] for e in index['entries'] if e['kind'] == 'capability'}
    if profiles != sources: errors.append('source/content membership differs')
    for e in index['entries']:
        if not set(e['source_ids']) <= sources: errors.append('unknown source: ' + e['id'])
        if not e.get('evidence'): errors.append('missing evidence: ' + e['id'])
    for catalog in index['tag_catalogs']:
        if catalog['source_id'] not in sources: errors.append('unknown catalog source')
        path = bundled_path(catalog['path'])
        if not path.is_file():
            errors.append('missing catalog: ' + catalog['id']); continue
        if hashlib.sha256(path.read_bytes()).hexdigest() != catalog['sha256']:
            errors.append('catalog hash differs: ' + catalog['id'])
        with path.open(encoding='utf-8-sig', newline='') as fh:
            count = sum(1 for _ in csv.DictReader(fh, delimiter=catalog['delimiter']))
        if count != catalog['rows_metadata']: errors.append('catalog row count differs: ' + catalog['id'])
    for error in errors: print('FAIL', error)
    print(f'CHECK sources={len(sources)} entries={len(ids)} errors={len(errors)} network_calls=0')
    return bool(errors)

def render(registry, index):
    lines = ['# 公开数据源与工具目录', '',
             f'快照日期：{index["checked"]}。覆盖 {len(registry["sources"])} 个来源说明、{len(index["entries"])} 条内容元数据。提供方目录、示例指标和工具声明的完整程度分别记录。', '',
             '查询方法见 [README](../README.md)，目录范围见 [publication-scope.json](publication-scope.json)。本文件由 `python scripts/lookup.py render` 生成。', '',
             '| 来源ID | 包含的数据 | 发现入口 | 访问条件 |', '|---|---|---|---|']
    for source in registry['sources']:
        values = [source['id'], source['content'], f'[{source["name"]}]({source["public_url"]})：{source["discovery"]}', source['access_requirements']]
        lines.append('| ' + ' | '.join(str(v).replace('|', '\\|').replace('\n', ' ') for v in values) + ' |')
    lines += ['', '## 可搜索的元数据目录', '', '| 目录ID | 来源 | 记录数 | 快照日期 |', '|---|---|---|---|']
    for catalog in index['tag_catalogs']:
        lines.append('| ' + ' | '.join(str(catalog[k]) for k in ['id','source_id','rows_metadata','checked']) + ' |')
    lines += ['', '记录数可能包含版本、视图、历史停止系列和层级节点。目录成员不保证有观测值、当前授权或接口兼容性。', '']
    target = ROOT / 'references/catalog.md'
    target.write_text('\n'.join(lines), encoding='utf-8', newline='\n')
    print('RENDER references/catalog.md')

def main():
    registry, index = load('registry.json'), load('data-index.json')
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    for command in ['list','check','render']: commands.add_parser(command)
    search = commands.add_parser('search'); search.add_argument('terms', nargs='+')
    show = commands.add_parser('show'); show.add_argument('id')
    data = commands.add_parser('data'); data.add_argument('terms', nargs='*')
    data.add_argument('--source'); data.add_argument('--kind'); data.add_argument('--limit', type=int, default=30)
    detail = commands.add_parser('data-show'); detail.add_argument('id')
    tags = commands.add_parser('tags'); tags.add_argument('terms', nargs='+')
    tags.add_argument('--catalog', choices=[c['id'] for c in index['tag_catalogs']]); tags.add_argument('--limit', type=int, default=20)
    args = parser.parse_args()
    if getattr(args,'limit',1) < 1: parser.error('--limit must be positive')
    if args.command == 'check': return check(registry, index)
    if args.command == 'render': render(registry, index); return 0
    if args.command in ['list','search']:
        for s in registry['sources']:
            if matches(s, getattr(args,'terms',[])): print(s['id'] + '\t' + s['name'] + '\t' + s['content'])
        return 0
    if args.command in ['show','data-show']:
        collection = registry['sources'] if args.command == 'show' else index['entries']
        entry = next((e for e in collection if e['id'] in {args.id,'source:' + args.id}), None)
        if not entry: parser.error('unknown ID: ' + args.id)
        if args.command == 'data-show':
            entry = {**entry,'related_sources':[s for s in registry['sources'] if s['id'] in entry['source_ids']]}
        print(json.dumps(entry, ensure_ascii=False, indent=2)); return 0
    if args.command == 'data':
        if args.source and args.source not in {s['id'] for s in registry['sources']}: parser.error('unknown source')
        selected = [e for e in index['entries'] if matches(e,args.terms)
                    and (not args.source or args.source in e['source_ids']) and (not args.kind or e['kind'] == args.kind)]
        for e in selected[:args.limit]: print(e['id'] + '\t' + e['name'] + '\t' + e['content'])
        print(f'DATA matched={len(selected)} shown={min(len(selected),args.limit)} network_calls=0'); return 0
    count, shown = 0, 0
    for catalog in index['tag_catalogs']:
        if args.catalog and args.catalog != catalog['id']: continue
        with bundled_path(catalog['path']).open(encoding='utf-8-sig',newline='') as fh:
            for row in csv.DictReader(fh,delimiter=catalog['delimiter']):
                if not matches(row,args.terms): continue
                count += 1
                if shown < args.limit:
                    print(json.dumps({'catalog':catalog['id'],'source_id':catalog['source_id'],'metadata':row},ensure_ascii=False)); shown += 1
    print(f'TAGS matched={count} shown={shown} network_calls=0'); return 0

if __name__ == '__main__':
    raise SystemExit(main())

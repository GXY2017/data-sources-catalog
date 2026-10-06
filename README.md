# Data Sources Catalog / 数据源与取数工具目录

整理数据源有哪些数据、从哪里发现指标、取数接口和访问条件。目录包含尚未下载的数据，可以按关键词、系列代码、股票代码或工具名查询。

本仓库提供 **84 个来源说明、3,927 条内容索引和 11 份可搜索的元数据目录**。每个来源都有官方或公开服务链接、查询方法、访问要求和目录完整程度。

## 内容

| 来源 | 已收录的元数据范围 |
|---|---|
| ECB | 215 条返回的数据流；9个已核DSD的维度和代码表 |
| BIS | 29 条返回的数据流，含房价、信贷、政策利率、跨境银行、衍生品等 |
| OECD | 1,548 条返回的数据流，含就业、物价、国民账户、投资、贸易、教育等 |
| Bundesbank | 94 条返回的数据流 |
| CFTC | 15 条门户资产，另有实际Socrata表字段定义 |
| Census | 1,809 条API数据集记录，包含年份、变量、分类和地理发现链接 |
| SEC | 10,434 条公司股票代码/CIK记录 |
| BOJ | 50个数据库目录；7库共66,885条系列/层级元数据，含65,223条有系列代码的记录 |
| 工具接口 | Yahoo 9个、A股30个、EDINET 11个、e-Stat 4个接口声明 |
| DataYes | 26个示例指标ID，提供方全目录未枚举 |

目录快照日期为 **2026-10-06**。记录数可能包含版本、发布视图、旧流、历史停止系列和层级节点，不能直接当作互不重复的可用指标数。公开目录、示例指标与工具声明的核验范围分别记录，目录成员不保证当前观测值、权限或接口兼容性。

## 查询

使用 Python 3.10+，只需标准库。查询不联网、不下载观测值，也不执行账户操作。

```sh
git clone https://github.com/GXY2017/data-sources-catalog.git
```

在克隆目录运行：

```sh
python scripts/lookup.py list
python scripts/lookup.py search 通胀
python scripts/lookup.py show ecb-sdmx
python scripts/lookup.py data 房价 --source bis-sdmx --kind upstream_dataflow
python scripts/lookup.py data 就业 --source oecd-cli --limit 5
python scripts/lookup.py data-show flow:ecb:ECB:EXR:1.0
python scripts/lookup.py tags EXR CURRENCY USD --catalog ecb-codes
python scripts/lookup.py tags ACS --catalog census-datasets --limit 5
python scripts/lookup.py tags FM08 Dollar --catalog boj-series --limit 5
python scripts/lookup.py tags AAPL --catalog sec-companies
python scripts/lookup.py data --source yfin-mcp --kind mcp_tool
python scripts/lookup.py data-show tool:estat:get_statistic_meta
python scripts/lookup.py check
```

多个关键词共同匹配。`data` 支持 `--source`、`--kind`、`--limit`；`tags` 支持 `--catalog` 和 `--limit`。中文别名用于发现，精确查询可用原始英文标题、流ID或代码。

完整来源表见 [catalog.md](references/catalog.md)，方法与口径见 [retrieval.md](references/retrieval.md)，导出范围见 [publication-scope.json](references/publication-scope.json)。

## 用作 Claude Code / Codex skill

根目录的 [SKILL.md](SKILL.md) 可作为 `data-sources-catalog` 用户级 skill。把仓库放在各客户端支持的 skill 目录，或在项目指令中指向 `SKILL.md`。保留已有私人配置，使用独立目录安装公开版本。

实际取数脚本、解释器、输出位置和维护项目由各自部署配置。本仓库登记公开发现接口与通用维护职责；私有部署可另建执行映射，不把账户凭据或个人路径写回公开目录。

## 数据边界

公开版仅含提供方描述、公开元数据、示例指标和工具接口。个人标识、账户/持仓/订单/现金流、机器地址、客户端配置、私人库结构、归档覆盖、内部项目路径、会话记录、备份和非公开订阅字典均已排除。凭据通过调用方自己的安全配置提供。

Citi、券商及付费服务保留访问条件，未附授权内容或账户可用性记录。查询脚本只读本仓库文件；需要观测值时，使用自身授权的官方接口，并核对单位、频率、实际/预期、复权及修订口径。

## 更新与许可

更新 JSON 权威记录后运行 `python scripts/lookup.py render` 和 `check`。公开目录刷新需按其官方端点重新取得元数据，保留机构、版本、维度顺序及日期。Census正式/BETA接口可能共用DCAT标识，索引ID附加数据集路径区分。

查询代码和原创说明采用 [MIT](LICENSE)。第三方元数据、统计名称及工具接口各自受提供方条款约束，MIT不改变它们的许可或授权。来源链接与快照日期保存在相应JSON中。本仓库不分发付费观测值或第三方完整报告。

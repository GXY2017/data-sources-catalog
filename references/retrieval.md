# 数据发现与取数方法

本文件给出提供方公开发现流程。具体适配器、认证及存储由各自部署维护。

## SDMX：ECB、BIS、OECD、Bundesbank

先读数据流目录，取得flow agency、id、version及引用的DSD（规定维度顺序和代码表的结构定义）。按匹配的DSD查维度及codelist，构造系列键，再取观测值。时间维度一般不放进系列键；不同流不能复用一套维度顺序。

| 提供方 | 公开发现端点与说明 |
|---|---|
| ECB | [dataflow](https://data-api.ecb.europa.eu/service/dataflow?references=none)，[元数据说明](https://data.ecb.europa.eu/help/api/metadata)，[数据查询](https://data.ecb.europa.eu/help/api/data) |
| BIS | [dataflow](https://stats.bis.org/api/v1/dataflow/BIS/all/latest?references=none)，[API说明](https://stats.bis.org/api-doc/v2/) |
| OECD | [dataflow](https://sdmx.oecd.org/public/rest/dataflow/all?references=none)，[官方API指南](https://www.oecd.org/en/data/insights/data-explainers/2024/09/api.html) |
| Bundesbank | [dataflow](https://api.statistiken.bundesbank.de/rest/metadata/dataflow/BBK?references=none)，[API说明](https://api.statistiken.bundesbank.de/doc/index.html) |

ECB EXR的系列键顺序为 `FREQ.CURRENCY.CURRENCY_DENOM.EXR_TYPE.EXR_SUFFIX`。`D.USD.EUR.SP00.A` 的代码属于已核维度代码表；目录本身没有证明该组合的当前观测值。

官方ECB结构查询形式：

```text
https://data-api.ecb.europa.eu/service/datastructure/<agency>/<structure-id>/<version>?references=all
```

观测值查询形式：

```text
https://data-api.ecb.europa.eu/service/data/<agency,flow-id,version>/<series-key>?format=csvdata&startPeriod=<start>&endPeriod=<end>
```

本仓库收录ECB的9个DSD，BIS/OECD/BBK全维度未枚举。取数实现应保留系列标识、单位、频率、状态和修订信息；只返回date/value的封装可能丢失口径。季度/周度期间需按频率解析。

## BOJ

[官方API手册](https://www.stat-search.boj.or.jp/info/api_manual_en.pdf)列出50个数据库。元数据接口：

```text
https://www.stat-search.boj.or.jp/api/v1/getMetadata?format=csv&lang=en&db=<DB>
```

先查数据库，再查 `SERIES_CODE`、名称、单位、频率与层级。已收录IR01、FM01、FM08、FM09、MD01、PR01、FF；其他数据库系列未完整枚举。空系列代码是层级节点。起止及更新日期属于元数据声明。

`getDataCode` 与 `getDataLayer` 取观测值，不能作为纯元数据检查接口。观测查询需遵守手册的请求上限、频率与续查规则。

## Census、FRED、e-Stat、SEC

- [Census目录](https://api.census.gov/data.json)：按数据集的 `c_variablesLink`、`c_groupsLink`、`c_geographyLink` 查看变量、分类与地理。全站API目录与ACES/AIES公开资本开支xlsx分别查询。正式/BETA接口有18组共用DCAT标识，使用数据集路径区别。
- [FRED API](https://fred.stlouisfed.org/docs/api/fred/)：先查categories/releases/series search和系列元数据，再查observations。需要自身API key；本仓库未枚举FRED系列全集。
- [e-Stat API](https://www.e-stat.go.jp/api/en/api-info)：关键词检索统计表，查表元数据和分类维度，再分页取数。app ID由调用方提供。不同年份版表ID会变化。
- [SEC API](https://www.sec.gov/search-filings/edgar-application-programming-interfaces)：股票代码/CIK目录不是全部filers，也不是财务taxonomy目录。CIK定位后分别查询submissions、companyfacts和concept，保留原申报链接及会计口径，遵守公平访问规则。

## CFTC

[公开目录](https://publicreporting.cftc.gov/data.json)包含数据集、展示页与帮助页。门户asset ID不自动等于可查询的Socrata数据表。

[`yw9f-hn96`](https://publicreporting.cftc.gov/api/views/yw9f-hn96.json)是 **TFF - Combined**，[`72hh-3qpy`](https://publicreporting.cftc.gov/api/views/72hh-3qpy.json)是 **Disaggregated - Futures Only**。以官方表定义和报告类型核对，保留futures-only与combined区别。本仓库字段快照排除了元数据响应内嵌的cachedContents样例与极值。

## 授权数据与口径

Citi可使用官方API或Excel插件的元数据与历史接口，授权按产品/标签核对。私人会话令牌不得提取或重放。券商市场数据、账户报表和订单接口分别配置；本仓库只记录市场数据发现。

ACES与AIES企业覆盖不同；投资累计同比与金额分开。名义/实际收益率、par/zero、现货/ETF代理、库存/仓单/off-warrant、卖空成交量/空头余额、期货隐含概率/预测市场价格均保留原名称与定义。

实际取数时交叉核对重要数值，记录时间、单位、调整、版本与原始来源。目录完整程度不证明某个账户拥有授权，也不证明所有维度组合都有观测值。

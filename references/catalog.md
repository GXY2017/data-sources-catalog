# 公开数据源与工具目录

快照日期：2026-10-06。覆盖 84 个来源说明、3927 条内容元数据。提供方目录、示例指标和工具声明的完整程度分别记录。

查询方法见 [README](../README.md)，目录范围见 [publication-scope.json](publication-scope.json)。本文件由 `python scripts/lookup.py render` 生成。

| 来源ID | 包含的数据 | 发现入口 | 访问条件 |
|---|---|---|---|
| fred | 宏观经济、就业、物价、利率、收益率与金融时间序列 | [FRED](https://fred.stlouisfed.org/docs/api/fred/)：categories / releases / series/search / series / series/observations | API key；先核指标、单位、频率与修订 |
| yahoo-market | 全球标的行情、OHLC、成交量与复权数据 | [Yahoo Finance 行情](https://finance.yahoo.com/)：symbol / period / interval | 数据授权、市场延迟与第三方接口限制 |
| citi-velocity | 外汇即期、远期点、波动率、OIS/IRS、国债、通胀互换、经济日历、预测及Citi指数 | [Citi Velocity](https://www.citivelocity.com/)：官方 API 或 Excel 插件元数据查询 | 客户登录及逐项数据授权；私人令牌不得提取或重放 |
| cme-irs | IRS/OIS曲线、期限、零息利率、贴现因子及利率报价 | [CME 利率曲线](https://www.cmegroup.com/market-data.html)：按曲线产品查官方数据分发及文件定义 | 分发方式、许可及报价类型需核对 |
| lch-swapclear | 利率互换清算相关曲线及结算利率 | [LCH SwapClear](https://www.lch.com/services/swapclear)：官方曲线文件：币种 / 产品 / 期限 / 发布日 | par/zero曲线口径分别保留 |
| government-yields | 多国名义、通胀挂钩及实际国债收益率 | [官方国债收益率](https://www.bankofcanada.ca/valet/docs)：按央行/财政部官方系列查询 | 固定期限、基准券、剩余期限和调查实际利率分开 |
| wgb-cds | 主权CDS、国债收益率与相关市场指标 | [World Government Bonds](https://www.worldgovernmentbonds.com/)：按国家 / 期限 / 日期检索 | 网站许可与历史覆盖；CDS bp及违约概率分开 |
| ecb-sdmx | 汇率、通胀、货币信贷、存贷款利率、收益率曲线、国民账户、国际收支、房价、调查和金融压力 | [ECB SDMX](https://data-api.ecb.europa.eu/service/dataflow?references=none)：dataflow → datastructure/codelist → data/<flow>/<key> | 公开元数据；观测值组合与频率兼容性需另核 |
| bbk-real-rate | 德国货币金融、银行、利率、汇率等；含调查预期实际利率 | [Bundesbank SDMX](https://api.statistiken.bundesbank.de/rest/metadata/dataflow/BBK?references=none)：metadata/dataflow → datastructure/codelist → data | 调查通胀预期扣除名义收益率与通胀挂钩债券收益率分开 |
| cfets | 人民币利率互换、USDCNY期权波动率、CDS及RMBS指数 | [CFETS 中国货币网](https://www.chinamoney.com.cn/)：按产品及日期查询官网数据 | 网站接口、历史长度与数据许可需核对 |
| dukascopy | 外汇BID/ASK历史报价、ticks与OHLC | [Dukascopy](https://www.dukascopy.com/swiss/english/marketwatch/historical/)：按instrument / UTC时间 / tick或bar查历史目录 | 点差、时间区与报价侧分开；许可按提供方条款 |
| oanda-v20 | instrument列表、外汇报价及历史candles | [OANDA v20](https://developer.oanda.com/rest-live-v20/introduction/)：accounts/instruments / instruments/<instrument>/candles | 需要自身账户和API授权；SIM/LIVE与报价侧分别核对 |
| dtcc-fx-options | OTC外汇期权公开成交、币种、名义本金、执行价、到期及交易事件 | [DTCC 公开交易报告](https://pddata.dtcc.com/)：按公开报告日期下载并按产品筛选 | 成交报告不能直接当作持仓；更正、撤销与重复事件需处理 |
| te-calendar | 经济日历的actual / previous / forecast / consensus、发布日期及重要性 | [Trading Economics 日历](https://docs.tradingeconomics.com/)：calendar；其他provider指标API单独发现 | API订阅和网页许可；实际值与预期分列 |
| atlanta-fed-mpt | SOFR期权隐含风险中性利率分布、期望值、分位数及概率 | [Atlanta Fed Market Probability Tracker](https://www.atlantafed.org/cenfis/market-probability-tracker)：官方历史下载及统计说明 | 合约参考窗口不自动等于逐次FOMC会议 |
| cftc-socrata | Legacy、Disaggregated、TFF及Supplemental/CIT周度持仓、未平仓量、变动、人数与集中度 | [CFTC Public Reporting](https://publicreporting.cftc.gov/data.json)：门户资产 → api/views/<id>.json字段 → 实际Socrata数据表 | 门户展示页与数据表分开；futures-only/combined分别保留 |
| bis-sdmx | 政策利率、有效汇率、房价、信贷、偿债率、跨境银行、流动性、债券、衍生品及支付 | [BIS SDMX](https://stats.bis.org/api/v1/dataflow/BIS/all/latest?references=none)：dataflow → matching DSD/codelists → data/<flow>/<key> | 流ID、版本、频率、单位、维度需按官方结构核对 |
| oecd-cli | CLI、就业、物价、国民账户、贸易、投资、税收、教育、医疗与环境统计 | [OECD SDMX](https://sdmx.oecd.org/public/rest/dataflow/all?references=none)：agency / flow-id / version → DSD → series key | 流版本与发布视图可重复；完整维度未全部枚举 |
| arab-opinion-index | 阿拉伯地区国家、调查波次、问卷及人口分组的民意调查统计 | [Arab Opinion Index](https://arabindex.dohainstitute.org/)：官方报告、问卷及开放数据目录 | 问卷/国家/年份/样本与权重分别核对；未附授权数据副本 |
| google-trends | 关键词按时间和地区的搜索兴趣相对指数 | [Google Trends](https://trends.google.com/trends/)：keyword / geography / period | 窗口与归一化影响可比性，指数不是搜索绝对数量 |
| epu | 经济政策不确定性、地缘政治风险及相关指数 | [Economic Policy Uncertainty / GPR](https://www.policyuncertainty.com/)：按官方指数与国家目录下载 | 更新日期、方法与指数系列口径需核对 |
| macrofinance | 宏观与资产指标目录、外汇及市场时间序列 | [Macrofinance / MacroVar](https://macrovar.com/)：按提供方指标目录检索 | 未附订阅目录或归档数据；最新覆盖与许可另核 |
| census-capex | 企业资本开支、构筑物、设备、软件与行业；全站目录另含人口、就业、住房、收入及贸易 | [Census ACES / AIES 及全站API目录](https://api.census.gov/data.json)：全站目录 → variables/groups/geography；ACES/AIES另查公开xlsx | ACES与AIES企业覆盖不同；全站目录不证明通用取数已实现 |
| axis-ai-capex | AI公司资本开支事件及SEC原始披露链接 | [Axis AI Capex Tracker](https://axis-intelligence.com/ai-capex-tracker/)：公开下载与媒体目录；entry × metric长表 | 遵循来源许可与网站验证；实际、指引及待核数据分开 |
| nbs-industry-fai | 分行业固定资产投资累计同比、行业分类与历史分类变化 | [国家统计局分行业投资](https://data.stats.gov.cn/)：指标树 → 指标元数据 → 日期与地区筛选 | 分行业金额与累计同比不可混用；使用官方允许的浏览器流程 |
| wgc-goldhub | 黄金供需、用途分项、投资及储备等统计 | [World Gold Council Goldhub](https://www.gold.org/goldhub/data)：官方数据目录、报告及下载 | 目录、报告期与可下载许可分别核对 |
| squeezemetrics-dix | DIX、GEX及相关市场指标 | [SqueezeMetrics](https://squeezemetrics.com/monitor/dix)：官方指标页面与公开下载 | 衍生指数方法、历史及许可需核对 |
| finra-regsho | 每日short volume、short-exempt volume及total volume | [FINRA Reg SHO](https://www.finra.org/finra-data/browse-catalog/short-sale-volume-data)：按报告日 / 市场下载官方文件 | 卖空成交量不等于空头余额 |
| alphaquery | 股票及期权统计、波动率和不同窗口指标 | [AlphaQuery](https://www.alphaquery.com/)：ticker / indicator / period | 字段、订阅与最新接口未全量核验 |
| tiingo | 股票/ETF历史行情及其他订阅数据API | [Tiingo](https://www.tiingo.com/documentation/general/overview)：官方API按ticker及数据产品查询 | API key、订阅及复权字段另核 |
| datayes | 宏观、行业与商品指标；示例含商品库存、欧元区/英国PMI、通胀、信心、房价及就业 | [DataYes 萝卜投研](https://robo.datayes.com/)：按indicator_id及提供方元数据查询 | 示例ID不构成提供方全目录；登录/订阅及接口另核 |
| wencai | 自然语言条件选股、筛选结果及汇总 | [同花顺问财](https://www.iwencai.com/)：自然语言query → 返回字段 | 字段随query变化；接口与使用条款需核对 |
| shengyishe | 商品价格、产业链指数及行业价格统计 | [生意社](https://www.100ppi.com/)：按品种 / 日期 / 指数查官网 | 报价来源、单位、市场与许可需核对 |
| treasury-auctions | 国债待拍卖、新发行日程与拍卖结果 | [美国财政部拍卖](https://www.treasurydirect.gov/auctions/)：官方日程与拍卖结果目录 | 公告、竞标截止、结算及结果日分别保留 |
| tdx-binary | 股票、指数及板块的OHLC、成交量和成交额字段 | [通达信日线格式](https://www.tdx.com.cn/)：授权取得的行情文件 → 格式解析 | 本仓库无行情文件；股票与指数单位及复权需核对 |
| tdx-lhb | 席位、买卖金额、净买入、上榜原因及机构统计 | [龙虎榜](https://data.eastmoney.com/stock/tradedetail.html)：按交易日 / 标的查公开披露 | 席位身份、买卖方向与公告修订需核对 |
| tdx-limit-pools | 涨停/跌停、封板资金、成交额、换手率及连板 | [涨跌停池](https://quote.eastmoney.com/)：按交易日及标的查询行情接口 | 历史覆盖、更新时间与数据许可需核对 |
| tdx-holders | 股东/机构持股、持股变动及披露期 | [股东与机构持股](https://data.eastmoney.com/gdfx/)：标的 / 报告期 / 披露日 | 持股报告期与信息公布日不可混用 |
| tdx-online | 报价、分时、逐笔及盘口 | [行情与逐笔接口](https://www.tdx.com.cn/)：按授权行情服务和instrument查询 | 服务许可、延迟、订阅及字段另核 |
| moomoo-market | 合约发现、行情及历史K线 | [moomoo OpenAPI 行情](https://openapi.moomoo.com/moomoo-api-doc/en/)：官方market-data接口 | 登录和市场订阅；没有附账户记录 |
| ibkr-market | 合约定义、历史/实时行情及延迟报价 | [IBKR 市场数据](https://www.interactivebrokers.com/campus/ibkr-api-page/)：官方合约发现与市场数据接口 | 自身API连接和市场订阅；没有附账户/报表/执行入口 |
| saxo-openapi | 合约、报价与图表数据 | [Saxo OpenAPI](https://www.developer.saxo/openapi/learn)：官方reference-data / price / chart接口 | 自身OAuth及数据许可；SIM与LIVE分开 |
| shfe-stocks | 分仓库周度总库存与仓单库存 | [SHFE 库存](https://www.shfe.com.cn/)：官方交易数据 / 库存周报 | 总库存与仓单分列；重量单位核对 |
| ine-stocks | 国际铜等产品分仓库库存与仓单 | [INE 库存](https://www.ine.cn/)：官方库存周报 | 品种、仓库、库存状态与单位分别核对 |
| comex-copper-daily | 铜合约日度交易和报告数据 | [COMEX 铜日度报告](https://www.cmegroup.com/markets/metals/base/copper.html)：按官方铜产品与报告类型查询 | 报告分类与单位以文件定义为准 |
| comex-copper-stocks | registered / eligible / total铜库存 | [COMEX 铜库存](https://www.cmegroup.com/market-data.html)：官方仓库库存报告 | short tons与metric tonnes分别保留 |
| cme-other-metals | 其他金属合约及仓库库存报告 | [CME 其他金属](https://www.cmegroup.com/markets/metals.html)：按产品和报告查官方目录 | 每个产品报告的覆盖与单位另核 |
| lme-moi | 金属未平仓量、期货、期权、TAPO及期限桶 | [LME Market Open Interest](https://www.lme.com/Market-data/Reports-and-data)：官方Market Open Interest报告 | MOI是未平仓量；报告分发与许可需核对 |
| lme-off-warrant | 非仓单金属库存按地区及汇总统计 | [LME Off-warrant](https://www.lme.com/Market-data/Reports-and-data)：官方off-warrant库存报告 | 与在库仓单库存分别保留 |
| lme-cot | 交易者分类持仓、净仓、变动及人数 | [LME COT](https://www.lme.com/Market-data/Reports-and-data)：官方Commitment of Traders报告 | 交易者类型与聚合规则需核对 |
| copper-cftc | HG铜周度Disaggregated持仓：仅期货及期货加期权 | [COMEX 铜 CFTC](https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm)：官方COT目录 → 报告类型 → 铜市场代码 | 合约数与吨换算、期货/综合口径分别保留 |
| icsg-copper | 矿产铜、精炼铜、消费及供需平衡统计 | [ICSG 铜统计](https://icsg.org/)：官方统计公报与产品目录 | 公开摘要和订阅详细数据分别查许可 |
| cochilco-mines | 智利分矿山月度铜产量及铜行业统计 | [COCHILCO](https://www.cochilco.cl/)：官方统计及下载目录 | 矿山、月份、重量与修订核对 |
| bcrp-copper | 秘鲁可回收铜产量等月度统计 | [BCRP 铜统计](https://estadisticas.bcrp.gob.pe/estadisticas/series/)：官方系列目录与系列代码 | 单位及recovered copper口径保留 |
| minem-copper | 秘鲁矿产铜月度/年度及分企业产量 | [MINEM 铜统计](https://www.gob.pe/minem)：官方矿业统计公报 | fine copper与其他重量口径分开 |
| chile-copper-exports | 铜出口量、金额及生产相关统计 | [智利铜出口](https://si3.bcentral.cl/siete/)：智利央行系列目录 / 出口商品 | 金属重量、货物重量、币种及统计期分别核对 |
| baltic-shipping | BDI、BCI、BPI、BCTI等航运运价指数 | [Baltic Exchange](https://www.balticexchange.com/)：官方指数目录与授权分发 | 指数构成、更新日和订阅许可需核对 |
| china-customs-major | 主要商品月度进出口数量与金额 | [中国海关主要商品](http://www.customs.gov.cn/)：官网统计公告和主要商品表 | 商品重量与金属含量分开；累计/当月及币种核对 |
| un-comtrade | 双边贸易量和值，reporter/partner/flow/HS code | [UN Comtrade](https://comtradeapi.un.org/)：官方reference目录 → reporter / partner / period / commodity | API key及速率限制；重量不能直接当作金属吨 |
| miner-capex | 矿企实际资本开支与管理层指引、币种及项目范围 | [矿企资本开支披露](https://www.sec.gov/edgar/search/)：公司IR / 原始申报文档 | 指引与实际、期间、合并范围及币种分别记录 |
| nbs-copper-demand | 铜、家电、汽车产量及地产/电力投资相关统计 | [国家统计局需求指标](https://data.stats.gov.cn/)：国家数据库指标树与公开发布 | 产量、销量、投资及代理指标分开 |
| cpca-sales | 乘用车销量、分类、累计及同比统计 | [乘联会](http://www.cpcaauto.com/)：官方月度报告 | 批发、零售、乘用车及全汽车口径分开 |
| caam-sales | 汽车月度销量及分类统计 | [中汽协](http://www.caam.org.cn/)：官方统计发布 | 机构、车型、销量和累计口径分别核对 |
| electricity-demand | 全社会及分产业月度/累计用电量 | [中国用电量](https://www.nea.gov.cn/)：国家能源局统计发布 | 月度、累计、行业及单位核对 |
| policy-rate-probabilities | 由期货/OIS推导的会议概率与利率路径 | [政策利率隐含概率](https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html)：合约及会议日 → 模型概率 | 概率为衍生结果，保留合约、假设与来源；非通用已实现取数器 |
| prediction-markets | Polymarket/Kalshi事件价格、盘口、成交与公开合约信息 | [预测市场](https://docs.polymarket.com/)：官方只读事件 / market / orderbook查询 | 事件规则、结算、时间戳及价格/概率分别核对 |
| stock-news | 公司新闻、公告、研报及来源链接 | [股票新闻与公告](https://www.moomoo.com/news)：按公司、时间与消息类别检索 | 原始公告优先；日期、转载及研报观点分别保留 |
| web-research | 官方网站、公开网页与文档文本 | [公开网页与文档](https://www.w3.org/)：按来源发现 → 原文提取 | 网站授权和文档版权；本仓库不附受限文档正文 |
| academic-papers | 论文、工作论文及预印本元数据和原文链接 | [学术论文目录](https://docs.openalex.org/)：官方开放文献API和原始出版物 | 数据库元数据许可与全文版权分别处理 |
| sec-filings | 公司CIK、股票代码、submissions、companyfacts、concept及申报原文 | [SEC EDGAR](https://www.sec.gov/search-filings/edgar-application-programming-interfaces)：公司 → CIK → submissions/companyfacts/concept | SEC公平访问规则；taxonomy/tag与报告口径需核对 |
| finmcp | 公司资料、财报、报价、期权、分析师、新闻和筛选接口 | [FinMCP 公司与市场接口](https://finance.yahoo.com/)：使用自身已连接工具的实际声明发现接口 | 工具与上游来源需逐项核对；未附私人MCP配置 |
| yfin-mcp | Yahoo行情、财报、持有人、股息拆股、期权、新闻和分析师接口 | [yfin-mcp](https://pypi.org/project/yfin-mcp/)：按ticker / statement-type / holder-type / period / expiry调用工具 | 工具签名是元数据快照；连接、授权与当前响应另核 |
| china-stock-mcp | A股行情、财报、资金流、股东、估值、研报、宏观、国证指数及行业板块 | [china-stock-mcp](https://pypi.org/project/china-stock-mcp/)：按tool名 / 股票代码 / 指标 / 日期查询 | 工具快照未证明每个上游接口当前可用 |
| longbridge | 合约、市场行情、历史K线及公司行动相关查询 | [Longbridge OpenAPI](https://open.longbridge.com/)：官方market-data接口 | 自身API凭据和数据订阅；不附账户接口或交易流程 |
| edinet | 日本公司检索、申报/XBRL、财务科目、指标、跨期比较和定性章节 | [EDINET](https://disclosure2.edinet-fsa.go.jp/)：公司/申报编号 → 文档及财报科目 | 自身API访问及申报口径；工具声明见公开快照 |
| edinetdb | 日本申报公司标准化财务数据和原始申报链接 | [EDINETDB](https://edinetdb.jp/)：search companies → financials / filing links | 多年覆盖、会计准则、币种及服务许可需核对 |
| estat | 日本官方统计表、分类元数据、地区/时间代码和统计值 | [e-Stat](https://www.e-stat.go.jp/api/en/api-info)：search_statistics → get_statistic_meta → data分页 | API app ID与服务条款；统计表全集未枚举 |
| boj | 利率、汇率、货币、贷款、资产负债表、资金流量、短观、物价、政府债务及国际收支 | [Bank of Japan](https://www.stat-search.boj.or.jp/info/api_manual_en.pdf)：getMetadata(db) → SERIES_CODE / frequency / unit / layers | 50库目录，7库系列快照；其余未枚举；起止日仅元数据声明 |
| yujiantouzi | 宏观经济及投研看板、数据序列 | [宇见投研](https://www.yujiantouzi.com/)：按提供方看板元数据发现 | 登录/服务许可及全站范围未核；不附私有工具配置 |
| financial-datasets | 可选公司与金融数据服务；本目录未调用或枚举其当前接口 | [Financial Datasets](https://www.financialdatasets.ai/)：官方文档及自身授权接口 | 在实际调用前取得明确授权并核对API订阅；目录列出不等于可用 |
| jin10 | 新闻、日历及行情类数据服务；具体接口范围未验证 | [金十数据](https://www.jin10.com/)：官方产品目录及自身授权接口 | 访问与许可需另核；未附机器配置或账户信息 |
| japan-meti-retail | 日本百货/超市商品销售额、业态、地区及时间分类 | [METI 商业动态统计](https://www.meti.go.jp/statistics/tyo/syoudou/)：官网统计 / e-Stat按年份检索后查维度 | 年度表ID会变化；月度速报与年度入库分别核对 |
| japan-chainstore | 会员连锁店销售、既存店同比及部门别月报 | [Japan Chain Stores Association](https://www.jcsa.gr.jp/public/statistics.html)：官方月度索引与报告 | 会员样本、既存店及全部店统计分开 |
| nbs-investment-release | 固定资产投资总量、三次产业及部分行业累计同比 | [国家统计局投资发布](https://www.stats.gov.cn/sj/zxfb/)：按统计期查正式发布稿 | 发布表小于完整指标树；分行业金额与同比分开 |

## 可搜索的元数据目录

| 目录ID | 来源 | 记录数 | 快照日期 |
|---|---|---|---|
| ecb-flows | ecb-sdmx | 215 | 2026-10-06 |
| ecb-codes | ecb-sdmx | 131339 | 2026-10-06 |
| bis-flows | bis-sdmx | 29 | 2026-10-06 |
| oecd-flows | oecd-cli | 1548 | 2026-10-06 |
| bbk-flows | bbk-real-rate | 94 | 2026-10-06 |
| cftc-datasets | cftc-socrata | 15 | 2026-10-06 |
| census-datasets | census-capex | 1809 | 2026-10-06 |
| sec-companies | sec-filings | 10434 | 2026-10-06 |
| boj-databases | boj | 50 | 2026-10-06 |
| boj-series | boj | 66885 | 2026-10-06 |
| datayes-indicators | datayes | 26 | 2026-10-06 |

记录数可能包含版本、视图、历史停止系列和层级节点。目录成员不保证有观测值、当前授权或接口兼容性。

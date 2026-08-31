# 弧光按钮商店插件 (ARC Button Shop Plugin)

[![Codacy Grade](https://app.codacy.com/project/badge/Grade/6567c5684e5b4c6eb83b27aea6e425c9)](https://app.codacy.com/gh/DEVILENMO/EndstoneMC-ARC-Button-Shop-Plugin/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![版本](https://img.shields.io/badge/版本-1.0.1-blue.svg)](https://github.com/DEVILENMO/EndstoneMC-ARC-Button-Shop-Plugin)
[![EndStone](https://img.shields.io/badge/EndStone-0.10+-green.svg)](https://github.com/EndstoneMC/endstone)
[![Python](https://img.shields.io/badge/Python-3.13+-yellow.svg)](https://www.python.org/)

一个复古的 Minecraft 服务器按钮商店系统，基于 EndStone 框架开发。玩家可以使用按钮创建个人商店，实现便捷的物品交易和服务器经济互动。

## 🎯 功能特性

### 🛒 核心功能
- **按钮商店**: 使用按钮创建个人商店，直观易用
- **物品交易**: 支持所有游戏物品的买卖交易
- **以物易物**: 用物品 B 按设定比例兑换物品 A，不经过金钱与税收
- **智能UI面板**: 现代化图形界面，支持商店创建、管理、浏览
- **价格自定义**: 灵活设置物品单价，自主经营
- **库存管理**: 实时库存显示和补充功能
- **交易记录**: 完整的交易历史记录和统计
- **商店保护**: 自动保护商店按钮，防止恶意破坏

### 🔄 以物易物商店
- **双物品选配**: 先从背包选择给出物 A（创建时扣除上架），再选择收取物 B（仅作兑换模板，创建时不扣）
- **自定义比例**: 设置每份交易「给出 x 个 A ↔ 收取 y 个 B」，并支持自定义显示名
- **按份兑换**: 玩家输入兑换份数，一次交出 `份数×y` 个 B，获得 `份数×x` 个 A
- **店主经营**: 可随时补充给出物 A 库存；玩家交出的 B 进入「已收取物品」，店主可一键领取
- **系统无限易物**: OP 可将以物易物店「转换为无限商店」，变为系统无限发放 A、不囤积收取物的官方易物点
- **安全回滚**: 背包空间不足时退还已扣的代价物，避免丢物；不依赖经济插件即可交易

### 👑 OP 系统商店（官方/无限商店）
- **无限出售（系统商店）**: OP 创建商店时可选择「无限出售」——不消耗背包物品，库存无限，玩家购买时系统发放物品（收入不归个人，代表官方）
- **无限收购（系统商店）**: OP 可选择「无限收购」——不预扣预算，收购预算无限，玩家出售物品时系统支付金钱（代表官方回收）
- **无个人创建者**: 系统商店店主固定为系统本身，不绑定创建 OP 的个人信息，也不会出现在「我的商店」中
- **管理全部商店**: OP 在主面板可使用「管理全部商店（OP）」查看并管理服务器内所有玩家的商店
- **转换为无限商店**: OP 在任意商店的管理面板中可将该商店「转换为无限商店（系统商店）」，一键变为无限库存/预算的官方商店
- **系统商店标识**: 无限商店在列表和详情中显示「无限」库存/预算及 §e[系统] 标识
- **快速设置自动定价商店**: OP 使用 `/bs qs start` 后，手持物品右键按钮即可批量创建官方出售+回收商店，`/bs qs stop` 退出

### 📈 官方定价与动态价格波动
- **官方定价商店**: OP 可创建「官方定价出售/收购/二合一」商店，物品与基准价来自 `official_prices.yml`，无需从背包选物
- **分类浏览与显示名**: 按价目表分区选择物品，支持 `display_name` 中文显示，并可优先从背包已有物品筛选
- **需求驱动调价**: 根据累计交易额自动调整价格——玩家购买越多出售价越高，系统收购越多回收价越低
- **出售-回收联动**: 出售价上涨时，回收价可按配置比例同步上涨，避免套利空间失控
- **每日随机波动**: 每天随机选取若干物品，在配置范围内产生 ±% 的日波动，增加市场变化感
- **价格自动回归**: 价格偏离基准后按小时缓慢回归，长期保持经济稳定
- **商店级折扣**: 官方定价商店支持设置折扣/加价百分比，在动态价格基础上叠加
- **安全防护**: 当回收价高于或等于出售价时自动禁用回收，防止刷钱漏洞

### ⚡ 性能优化
- **区块化存储**: 智能区块索引，快速查找附近商店
- **缓存机制**: 高效的数据缓存，减少数据库查询
- **异步处理**: 非阻塞操作，确保服务器流畅运行
- **内存优化**: 智能内存管理，适合大型服务器

### 💰 经济与背包集成
- **经济系统集成**: 支持 ARC Core 或 UMoney（任意其一，自动识别）
- **弧光背包管理器**: **必须安装**独立插件 `arc_inventory` ≥ 0.1.4（优先公开 `api_*`）
- **自动交易**: 安全的资金转账和物品交换
- **防作弊**: 严格的交易验证和错误处理
- **多货币支持**: 支持服务器自定义货币系统
> 自动检测顺序：优先使用 `arc_core`，如果未安装则尝试 `umoney`；两者均不存在时，仅禁用金钱相关功能。

### 🌐 多语言支持
- **中英双语**: 完整的多语言界面支持
- **本地化**: 所有文本可自定义和本地化
- **可扩展**: 易于添加新语言包

## 📦 安装说明

1. **下载插件**: 将插件文件放置到服务器的 `plugins` 目录
2. **安装依赖**:
   - 经济：ARC Core 或 UMoney（任意其一；优先 `arc_core`）
   - 背包：**必须安装** [弧光背包管理器](https://github.com/ARC-Minecraft/EndstoneMC-ARC-Inventory-Manager)（`arc_inventory` ≥ 0.1.4）
3. **重启服务器**: 重启服务器或使用插件管理器重新加载
4. **自动初始化**: 插件将自动创建必要的数据库和配置文件
5. **开始使用**: 玩家可以使用 `/bs` 命令开始创建商店

## 🎮 使用指南

### 📋 指令详解

| 指令 | 权限要求 | 语法 | 功能描述 |
|------|----------|------|----------|
| `/bs` | 所有玩家 | `/bs` | 打开商店主面板，管理和浏览商店 |
| `/bs qs start` | OP | `/bs qs start` | 进入自动定价商店快速设置模式：手持物品右键按钮，即设为官方出售+回收商店 |
| `/bs qs stop` | OP | `/bs qs stop` | 退出自动定价商店快速设置模式 |
| `/shopmanage` | OP | `/shopmanage <list\|clear\|reload\|prices\|pricereload\|pricereset\|delns>` | 管理员商店与定价管理指令 |

### 🏪 创建商店流程

1. **打开界面**: 使用 `/bs` 命令打开商店主面板
2. **选择类型**: 点击「创建商店」，选择「出售商店」「收购商店」或「以物易物商店」；**OP 额外可选**「无限出售（系统商店）」「无限收购（系统商店）」或「官方定价」出售/收购/二合一
3. **选择物品**: 玩家店从背包选择物品；以物易物需先后选择给出物 A 与收取物 B；官方定价店按分类或背包筛选选择价目表物品（不消耗物品或预算）
4. **设置价格/比例**: 玩家买卖店输入单价；普通收购商店还需输入预算；以物易物设置兑换比例 x:y；官方定价店可设置折扣/加价百分比
5. **放置按钮**: 在想要创建商店的位置放置一个按钮
6. **右键激活**: 右键点击按钮完成商店创建（出售/以物易物会从背包扣除给出物 A）

### ⚡ 快速设置自动定价商店（OP）

1. 输入 `/bs qs start` 进入快速设置模式
2. 手持要上架的物品（未在 `official_prices.yml` 配置的物品会暂以 **99999** 作为出售价，后续补配置并 `/shopmanage pricereload` 即可生效）
3. 右键已放置的按钮，立即创建官方出售+回收二合一商店
4. 可连续更换手持物品并点击其他按钮批量建店
5. 输入 `/bs qs stop` 退出模式

### 💳 购买 / 兑换流程

1. **发现商店**: 右键/点击互动其他玩家创建的商店按钮
2. **查看详情**: 浏览商品信息、价格或兑换比例、库存等
3. **输入数量**: 买卖店选择购买数量；以物易物输入兑换份数（受库存与背包持有量限制）
4. **确认交易**: 买卖店处理资金与物品；以物易物扣除代价物 B 并发放给出物 A（不收税）

### 🔧 商店管理

#### 我的商店功能
- **库存管理**: 查看库存；出售店与以物易物店可随时「补充库存」（补充给出物 A），未售罄也可补货，数量由玩家自由填写（受背包持有量限制）
- **收取物品**: 收购店与以物易物店可将玩家交来的物品领取回背包
- **售罄可继续管理**: 库存售罄后商店仍可打开管理面板进行补货，不会因售罄而从列表/按钮交互中消失
- **价格调整**: 修改商品单价（计划中功能）
- **交易记录**: 查看销售历史和收入统计
- **商店删除**: 删除商店并取回剩余库存；以物易物店同时返还已收取的代价物
- **系统商店**: 无限商店显示「无限」库存/预算，无需补充库存或收取物品；店主显示为系统，不绑定个人

#### OP 管理功能
- **管理全部商店**: OP 在主面板点击「管理全部商店（OP）」可列出服务器内所有活跃商店，点击任意商店进行管理
- **转换为无限商店**: 在商店管理面板中，OP 可将该商店「转换为无限商店（系统商店）」——买卖店变为无限库存/预算；以物易物店变为系统无限发放 A 的官方易物点
- **官方定价管理**: 使用 `/shopmanage prices` 查看基准价与波动状态；`/shopmanage pricereload` 重载定价文件；`/shopmanage pricereset` 重置所有动态调整
- **按命名空间批量删除**: `/bs` 主面板（OP）或 `/shopmanage delns` 列出所有模组命名空间及商店数量；点击确认后删除该命名空间下全部商店（不含 `minecraft` 与无命名空间物品）。也可直接 `/shopmanage delns <命名空间>` 进入确认。模组卸载后清理残留商店很方便
- **删除他人商店**: OP 从「管理全部商店」删除他人商店时，剩余库存/预算及收集物品会返还给**店主**（店主在线则发放物品）

#### 商店保护机制
- **自动保护**: 商店按钮自动受到保护，防止恶意破坏
- **店主权限**: 只有店主可以破坏自己的商店按钮
- **智能返还**: 店主破坏按钮时自动返还剩余库存/预算
- **友好提示**: 非店主尝试破坏时显示友好提示信息

#### 附近商店浏览
- **智能搜索**: 基于区块快速查找附近商店
- **距离显示**: 显示商店与玩家的距离
- **商品预览**: 快速了解商店出售的商品

## 🔧 技术架构

### 区块化存储优化

插件采用智能区块索引系统，大幅提升性能：

#### 区块索引
- **16x16 区块划分**: 将世界按 Minecraft 标准区块大小划分
- **快速定位**: 玩家交互时先查区块索引，再精确查询位置
- **内存优化**: 避免遍历所有商店数据，性能提升数十倍

### 🏗️ 数据库设计

#### 核心表结构

**button_shops** - 商店信息表
- `shop_uuid` - 商店唯一标识
- `owner_xuid` - 店主XUID（主要标识符，永不变更）
- `owner_name` - 店主名称（用于显示）
- `shop_type` - 商店类型：`sell` 出售 / `buy` 收购 / `barter` 以物易物 / `both` 出售+回收（官方定价）
- `is_infinite` - 是否为系统无限商店；系统店 `owner_xuid`/`owner_name` 为 `SYSTEM`
- `x/y/z/dimension` - 商店位置和维度
- `chunk_x/chunk_z` - 区块坐标（索引优化）
- `item_type/item_data` - 商品信息（含附魔、Lore 等）
- `quantity/stock` - 商品数量和库存（无限商店为特殊值表示无限）
- `unit_price` - 单价
- `is_infinite` - 是否无限商店（系统/官方商店，0=否 1=是）
- `create_time` - 创建时间

**chunk_index** - 区块索引表  
- `chunk_x/chunk_z/dimension` - 区块坐标
- `shop_count` - 该区块商店数量

**shop_transactions** - 交易记录表
- `shop_id` - 关联商店ID
- `buyer_xuid` - 买家XUID（主要标识符）
- `buyer_name` - 买家名称（用于显示）
- `quantity/total_price` - 交易数量和金额
- `transaction_time` - 交易时间

> 💡 **XUID说明**：插件使用玩家的XUID作为主要标识符，这确保了即使玩家更改游戏名称，其商店和交易记录仍然保持关联。玩家名称仅用于界面显示。

### 📡 API 接口文档

插件提供完整的 API 接口供其他插件调用：

#### 商店查询接口

##### `api_get_shop_at_position(x: int, y: int, z: int, dimension: str) -> dict | None`
获取指定位置的商店信息
```python
shop_plugin = server.plugin_manager.get_plugin("arc_button_shop")
shop = shop_plugin.api_get_shop_at_position(100, 64, -50, "overworld")
if shop:
    print(f"店主: {shop['owner_name']}")
    print(f"商品: {shop['item_type']}")
    print(f"库存: {shop['stock']}")
```

##### `api_get_player_shops(player_xuid: str) -> list`
获取玩家的所有商店（基于XUID）
```python
player_xuid = "12345678901234567890"  # 玩家的XUID
player_shops = shop_plugin.api_get_player_shops(player_xuid)
print(f"玩家拥有 {len(player_shops)} 个商店")
for shop in player_shops:
    print(f"位置: ({shop['x']}, {shop['y']}, {shop['z']})")
    print(f"店主: {shop['owner_name']}")
```

##### `api_get_nearby_shops(x: int, z: int, dimension: str, radius: int = 1) -> list`
获取指定位置附近的商店（基于区块）
```python
nearby = shop_plugin.api_get_nearby_shops(100, -50, "overworld", radius=2)
print(f"附近有 {len(nearby)} 个商店")
```

#### 交易接口

##### `api_purchase_from_shop(shop_id: int, buyer_xuid: str, quantity: int) -> tuple[bool, str]`
从商店购买商品（基于XUID）
```python
buyer_xuid = "98765432109876543210"  # 买家的XUID
success, message = shop_plugin.api_purchase_from_shop(
    shop_id=123,
    buyer_xuid=buyer_xuid,
    quantity=5
)
if success:
    print("购买成功")
else:
    print(f"购买失败: {message}")
```

##### `api_get_all_active_shops() -> list`
获取所有活跃的商店
```python
all_shops = shop_plugin.api_get_all_active_shops()
print(f"服务器共有 {len(all_shops)} 个活跃商店")
```

### API 使用示例

```python
# 完整的商店系统集成示例
class EconomyPlugin(Plugin):
    def on_enable(self):
        # 获取商店插件实例
        self.shop = self.server.plugin_manager.get_plugin("arc_button_shop")
        
    def get_market_stats(self):
        """获取市场统计信息"""
        all_shops = self.shop.api_get_all_active_shops()
        
        stats = {
            'total_shops': len(all_shops),
            'total_items': sum(shop['stock'] for shop in all_shops),
            'average_price': sum(shop['unit_price'] for shop in all_shops) / len(all_shops) if all_shops else 0,
            'top_sellers': self._get_top_sellers(all_shops)
        }
        
        return stats
    
    def create_automated_shop(self, location, item_data, price):
        """自动创建商店（管理员功能）"""
        # 这里可以集成自动商店创建逻辑
        pass
```

## 📊 数据存储

插件使用 SQLite 数据库进行数据持久化存储：

**数据库文件位置**: `plugins/ARCButtonShop/button_shop.db`

### 存储优势
- **轻量级**: SQLite 无需独立服务器，内嵌式存储
- **高性能**: 针对商店查询进行索引优化
- **数据安全**: 支持事务，确保交易数据一致性
- **易维护**: 单文件数据库，便于备份和迁移

## ⚙️ 配置系统

### 🌐 语言文件配置

语言文件位于项目根目录：
- `CN.txt` - 中文语言包
- `EN.txt` - 英文语言包

### 自定义文本

您可以编辑语言文件来自定义所有游戏内提示信息：

```ini
# CN.txt 示例 - 商店系统文本
SHOP_MAIN_PANEL_TITLE=§6按钮商店系统
SHOP_CREATE_BUTTON=§a创建商店
SHOP_PURCHASE_SUCCESS=§a购买成功！获得 {0} 个 {1}，花费 {2}
SHOP_SALE_NOTIFICATION=§a你的商店有新交易！§f{0} 购买了 {1} 个 {2}，收入 {3}
# ... 更多配置项
```

### 配置参数

插件配置文件位于 `plugins/ARCButtonShop/`：

#### `core_setting.yml` — 全局设置（`key=value` 格式）

除交易税、商店数量限制外，动态定价相关配置也由此文件管理：

```ini
# 交易税
trade_tax_enabled=true
trade_tax_rate=0.05
max_shops_per_player=50

# 动态定价总开关
dynamic_pricing_enabled=true

# 需求驱动调价
dynamic_pricing_sell_amount_per_percent=10000   # 每累计出售交易额达此金额，出售价涨 1%
dynamic_pricing_buy_amount_per_percent=10000    # 每累计收购交易额达此金额，回收价降 1%
dynamic_pricing_max_sell_increase=0.50          # 出售价最大涨幅（50%）
dynamic_pricing_max_buy_decrease=0.30           # 回收价最大降幅（30%）
dynamic_pricing_sell_buy_link_ratio=0.5         # 出售涨价时回收价联动比例（0=关闭，1=完全同步）
dynamic_pricing_recovery_rate_per_hour=0.0002   # 每小时向基准价回归速率（约两天恢复 1%）

# 每日随机波动
daily_fluctuation_enabled=true
daily_fluctuation_item_count=3                  # 每日随机波动的物品种类数
daily_fluctuation_min_percent=-15               # 波动下限（%）
daily_fluctuation_max_percent=15                # 波动上限（%）
daily_fluctuation_reset_hour=0                  # 每日重置时间（24 小时制，0=午夜）
```

#### `official_prices.yml` — 官方基准定价

定义各物品的基准出售价与回收价（仅价格数据，不含动态定价开关）：

```yaml
prices:
  minecraft:diamond:
    sell: 1000    # 玩家购买单价（基准）
    buy: 500      # 玩家出售给商店单价（基准）
  minecraft:iron_ingot:
    sell: 50
    buy: 25
```

最终成交价 = 基准价 × (1 + 需求调整 + 日波动) × (1 + 商店折扣%)。

```python
# 插件内置参数
CHUNK_SIZE = 16              # 区块大小（标准 Minecraft 区块）
```

### 🎒 背包操作集成

插件基于 [EndStone Inventory API](https://endstone.dev/latest/reference/python/inventory/) 实现了完整的背包操作：

#### 支持的操作
- **📦 物品检测**：自动扫描玩家背包中的所有物品
- **➖ 物品移除**：安全地从背包中移除指定数量的物品  
- **➕ 物品添加**：智能地将物品添加到背包空位
- **🔍 库存验证**：交易前验证物品和资金充足性

#### 背包API特性
```python
# 基于EndStone标准API
inventory = player.inventory
item_stack = inventory.get_item(slot_index)
inventory.add_item(item_stack)
inventory.set_item(slot_index, item_stack)

# 支持ItemStack属性
item_stack.type      # 物品类型
item_stack.amount    # 物品数量  
item_stack.data      # 物品数据值
item_stack.item_meta # 物品元数据
```

#### 安全机制
- **事务性操作**：确保物品和金钱的原子性转移
- **错误恢复**：操作失败时自动回滚所有变更
- **背包检查**：防止背包满时的物品丢失

## 🛡️ 系统要求

- **EndStone**: 0.10 或更高版本  
- **Python**: 3.13 或更高版本
- **经济插件**: ARC Core 或 UMoney（二选一，自动识别）
- **操作系统**: Windows, Linux, macOS
- **内存**: 建议至少 1GB 可用内存
- **存储**: 约 5MB 磁盘空间（不含数据库增长）

## 🎮 使用场景

### 🏪 玩家经济服务器
- 建立完整的玩家交易生态系统
- 支持大型商业区建设
- 实现去中心化的商品流通

### 🏛️ 城镇建设服务器  
- 每个城镇可建立特色商店集群
- 支持区域性商业发展
- 促进玩家间合作与竞争

### 🎲 生存/冒险服务器
- 资源交易和装备买卖
- 稀有物品拍卖系统
- 探险收获变现渠道

### 🎪 小游戏服务器
- 游戏奖励兑换商店
- 临时活动商品销售
- 积分消费和奖品发放

## 📝 更新日志

### v1.0.1 (当前版本)

- 🔗 背包操作改为优先走 `arc_inventory` 公开 `api_*`（兼容 0.1.4+ `remove_item` 返回数量），底层 `InventoryManager` 仅作回退
- 📦 建议同步升级弧光背包管理器至 ≥ 0.1.4

### v1.0.0

大版本：官方商店架构与木牌商店对齐，定价系统外迁至弧光市场经济插件。

- ✅ **指令格式对齐木牌商店**：`/bs qs (start|stop)` 单条枚举重载；`/shopmanage` 补全子命令 usages
- ✅ **商店类型精简为五种**：玩家出售/收购/交换 + 官方出售/官方回收（OP）
- ✅ **官方店默认二合一 + 市场经济**：自动定价走 `arc_market_economy` API；管理面板可单独关闭出售或回收
- ✅ **手动定价**：官方出售/回收入口可选固定单价无限店
- ✅ **快速设置**：`/bs qs start [both|sell|buy]`，缺失价目自动写入 0 元占位
- ⚠️ **破坏性变更**：移除内嵌 `PriceManager` 与本地动态定价表，自动定价需安装 `arc_market_economy`

### v0.5.0

- （内容已并入 v1.0.0，此版本仅作过渡发布记录）

### v0.4.6

- ✅ 成交记录写入弧光核心天眼（`ShopTrade`），需 arc_core ≥ 0.8.12 且 `ENABLE_SKY_EYE=True`
- ✅ `/bs` 命令与 OP 快速设置官方店（`/bs qs start|stop`）等此前未推送改动一并发布

### v0.4.5

- 🏷️ **快速设置占位定价**：未在 `official_prices.yml` 配置的物品可照常建店，暂以 99999 作为出售价；补配置并 `pricereload` 后自动切换为正式官方定价

### v0.4.4

- 🔁 **主指令改为 `/bs`**：原 `/shop` 已替换为 `/bs`（ArcCore 主菜单入口同步调用 `/bs`）
- ⚡ **快速设置自动定价商店**：OP 使用 `/bs qs start` 进入模式后，手持物品右键按钮即可创建官方出售+回收二合一商店；未配置官方定价的物品暂以 99999 作为出售价，`/bs qs stop` 结束

### v0.4.3

- 确认并整理近期修复说明（需同时安装弧光背包管理器 `arc_inventory` ≥ 0.1.3）

#### 交易崩溃
- 🩹 **购买/收购时报 `has_item`**：商店按插件名比背包管理器先启用，`inventory_manager` 仍为 `None` 就会直接报错。现已声明硬依赖 `arc_inventory`，交易时还会再尝试挂载管理器

#### 物品发放
- 🪓 **删店退货数量不对**：镐等不可堆叠物品曾按 64 一叠发放，7 把镐可能只退回 1～2 把（已由背包管理器按真实堆叠上限逐个发放）
- 📖 **附魔书买到手是白板**：经验修补等带 NBT 的附魔书还原失败后不会回退写附魔（已由背包管理器修复）

#### 依赖
- 🎒 彻底移除本包内嵌背包实现，**必须安装** `arc_inventory`

### v0.4.2
- 🩹 **修复交易空引用**：声明硬依赖 `arc_inventory`，并在买卖/易物时延迟挂载背包管理器，避免商店比背包插件先启用导致 `has_item` 报错

### v0.4.1
- 🎒 **强制依赖弧光背包管理器**：移除本包内嵌 `InventoryManager`，未安装 `arc_inventory` 时禁用物品操作
- 🔗 删店/领取返还改为按 `give_item_count` 实际入包数量提示与记日志（配合背包管理器修复不可堆叠物数量丢失）

### v0.4.0

#### 以物易物
- 🔄 **以物易物商店**：新建商店类型，玩家用物品 B 按比例兑换物品 A，全程不经金钱与交易税
- ⚖️ **自定义兑换比例**：创建时先后选择给出物 A、收取物 B，并设置每份交易的 x:y 数量
- 📦 **库存与收取**：创建时上架 A；可随时补货 A；玩家交出的 B 记入已收取物品，店主可领取
- ♾️ **系统无限易物**：OP 可将以物易物店转换为系统无限商店，无限发放 A
- 🛡️ **交易安全**：背包满时退还已扣代价物；删除商店时返还剩余 A 与已收取的 B

#### 体验与文案
- 🔙 **选物面板返回**：创建流程中返回键回到上一步类型/选物面板，而不是直接回主面板
- 🌐 **中英文语言包**：补充以物易物相关界面文案

### v0.3.3

- 🎒 **弧光背包管理器**：优先使用独立插件 `arc_inventory` 操作背包；未安装时仍回退内嵌实现

### v0.3.2

#### 管理功能
- 🗑️ **按命名空间批量删除**：OP 可通过 `/shop` 主面板或 `/shopmanage delns` 列出模组命名空间并一键删除该命名空间下全部商店（排除 `minecraft` 与无命名空间物品）；支持 `/shopmanage delns <命名空间>` 直达确认

### v0.3.1

#### 系统商店与玩家补货
- 🏷️ **系统商店不记创建者**：无限/官方系统店店主固定为 `SYSTEM`，界面显示「系统（官方商店）」，不再绑定创建 OP，也不会出现在「我的商店」
- 📦 **随时补货**：玩家出售店管理面板始终提供「补充库存」，未售罄也可补货
- ✍️ **自由数量**：补货数量由玩家自行填写任意正整数（受背包持有量限制）
- 🔄 **售罄仍可管理**：售罄后不再将商店停用隐藏，店主可继续打开按钮/管理面板补货；旧库售罄停用店启动时自动恢复

#### 官方定价体验增强
- 🔀 **二合一官方店**：支持同一按钮同时出售与回收（`both`）
- 📂 **分类选物**：按 `official_prices.yml` 分区浏览，支持 `display_name` 与背包物品优先筛选
- 🧾 **价目与文案**：扩充官方价目表与中英文语言文件

### v0.3.0

#### 官方定价与动态价格波动
- 📈 **官方定价商店**：OP 可创建官方定价出售/收购商店，基准价由 `official_prices.yml` 统一管理
- 📊 **需求驱动调价**：根据累计交易额自动涨跌价，支持涨幅/降幅上限与出售-回收联动
- 🎲 **每日随机波动**：每天随机选取物品产生 ±% 波动，可配置种类数、范围与重置时间
- ⏳ **价格自动回归**：每小时向基准价缓慢回归，防止价格长期偏离
- ⚙️ **配置分离**：动态定价开关与参数迁移至 `core_setting.yml`，`official_prices.yml` 仅保留基准价
- 🛡️ **回收保护**：回收价高于出售价时自动禁用回收，防止套利
- 🔧 **管理命令**：新增 `/shopmanage prices`、`pricereload`、`pricereset` 子命令

### v0.2.2

#### 最近修复更新
- 🩹 **购买与背包满时的经济漏洞修复**：出售商店购买改为**先尝试发放物品，再按实际成功发放的数量**扣款、计税、扣库存并记账。修复此前在背包空间不足、物品只能部分进包时，错误触发全额退款路径，导致**少扣或不扣买家钱**的问题；若实际发放少于输入数量，会提示本次仅成功购买的数量。
- 🧮 **发放数量 API**：`InventoryManager` 新增 `give_item_count`，返回实际发放数量；`give_item` 据此判断是否足额发放，便于上层按真实到账量结算。

### v0.2.1

#### 最近修复更新
- 🩹 **NBT兼容修复**：增加对更新后 NBT 结构的支持，确保物品数据读取与识别更加稳定
- 🔄 **数据兼容性优化**：针对新版 NBT 变化优化了商店物品信息处理流程，降低因数据格式变动导致的异常风险

### v0.2.0

#### 基础功能
- ✨ 全新的按钮商店系统
- 🎨 现代化UI面板界面
- 🌍 完整多语言支持（中英双语）
- ⚡ 区块化存储优化，大幅提升性能
- 💰 经济系统集成：支持 ARC Core 或 UMoney（二选一）  
- 🔌 完整的API接口供其他插件调用
- 📊 SQLite数据库高效存储
- 🛒 支持商店管理、库存补充、交易记录
- 🔍 智能附近商店搜索功能
- 🆔 **XUID支持**：使用玩家XUID确保数据永久关联
- 🎒 **标准背包API**：基于EndStone官方inventory API
- 🔒 **事务安全**：完整的交易回滚和错误恢复机制
- 🛡️ **商店保护**：自动保护商店按钮，防止恶意破坏

#### OP 与系统商店（新增）
- 👑 **无限出售（系统商店）**：OP 创建商店时可选择「无限出售」——不消耗背包物品、库存无限，玩家购买时由系统发放物品（代表官方）
- 👑 **无限收购（系统商店）**：OP 可选择「无限收购」——不预扣预算、预算无限，玩家出售物品时由系统支付金钱（代表官方回收）
- 📋 **管理全部商店**：OP 主面板新增「管理全部商店（OP）」入口，可查看并管理服务器内所有商店；删除他人商店时返还给店主
- 🔄 **转换为无限商店**：OP 在任意商店管理面板可将该商店「转换为无限商店（系统商店）」
- 🏷️ **系统商店标识**：无限商店在列表中显示「无限」库存/预算及 §e[系统] 标识；数据库新增 `is_infinite` 字段并支持旧库自动迁移

## 🤝 贡献指南

我们热烈欢迎社区贡献！

### 🐛 报告问题
- 使用 GitHub Issues 报告 bug
- 提供详细的错误信息和复现步骤
- 包含 EndStone 版本和插件版本信息
- 附上相关的日志文件

### 💡 功能建议
- 在 Issues 中提出新功能建议  
- 详细描述功能需求和使用场景
- 考虑功能的可行性和实用性
- 参与社区讨论和投票

### 👨‍💻 代码贡献
- Fork 项目并创建功能分支
- 遵循 PEP 8 Python 代码风格
- 添加必要的单元测试
- 更新相关文档
- 提交清晰的 Pull Request

### 🌍 本地化支持
- 翻译语言文件到其他语言
- 改进现有翻译质量
- 适配不同地区的使用习惯

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE)，您可以：
- ✅ 自由使用和修改源代码
- ✅ 用于商业和非商业目的  
- ✅ 分发修改后的版本
- ⚠️ 需要保留原始许可证声明

## 📞 技术支持

获取帮助的多种方式：

- 📧 **邮箱支持**: DEVILENMO@gmail.com
- 🐛 **问题反馈**: [GitHub Issues](https://github.com/DEVILENMO/EndstoneMC-ARC-Button-Shop-Plugin/issues)
- 💬 **社区讨论**: 参与项目讨论区
- 📚 **文档中心**: 查阅完整文档和教程

### 常见问题快速解答
1. **Q**: 插件需要哪些依赖？  
   **A**: 需要安装经济插件中的任意一个：ARC Core 或 UMoney（插件会自动检测并优先使用 ARC Core）。

2. **Q**: 如何备份商店数据？  
   **A**: 复制 `plugins/ARCButtonShop/button_shop.db` 文件

3. **Q**: 商店数量有限制吗？  
   **A**: 目前无限制，后续版本将添加配置选项

---

**🛒 弧光按钮商店插件** - 打造您的 Minecraft 服务器专属经济生态！

*Built with ❤️ for the Minecraft community by DEVILENMO*

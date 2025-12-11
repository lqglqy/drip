# Repository 层

数据库访问层，实现数据持久化操作。

## 主要组件

- **DataAssetRepository** - 数据资产数据访问
- **BackupRecordRepository** - 备份记录数据访问
- **JobRepository** - 任务记录数据访问
- **PolicyRepository** - 策略配置数据访问
- **TenantRepository** - 租户信息数据访问

## 模式

使用 Repository Pattern 隔离数据访问逻辑，提供清晰的数据库接口。

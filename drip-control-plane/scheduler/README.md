# Scheduler 层

分布式调度和定时任务模块。

## 主要组件

- **ScanJobScheduler** - 数据扫描任务调度器
- **BackupJobScheduler** - 数据备份任务调度器

## 功能

- 定时触发扫描和备份任务
- 支持分布式环境下的任务协调
- 任务执行状态跟踪

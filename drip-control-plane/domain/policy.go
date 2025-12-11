package domain

import "time"

// Policy 策略配置领域模型
type Policy struct {
    ID             string    `json:"id"`
    TenantID       string    `json:"tenant_id"`
    Name           string    `json:"name"`
    Description    string    `json:"description"`
    PolicyType     string    `json:"policy_type"` // SCAN, BACKUP, RETENTION, ALERT
    Enabled        bool      `json:"enabled"`
    ScoringRuleID  string    `json:"scoring_rule_id"` // 关联的评分规则
    ScanInterval   int       `json:"scan_interval"`   // 扫描间隔（分钟）
    BackupInterval int       `json:"backup_interval"` // 备份间隔（分钟）
    RetentionDays  int       `json:"retention_days"`  // 保留天数
    AlertThreshold int       `json:"alert_threshold"` // 告警阈值
    Priority       string    `json:"priority"`        // HIGH, MEDIUM, LOW
    CreatedBy      string    `json:"created_by"`
    CreatedAt      time.Time `json:"created_at"`
    UpdatedAt      time.Time `json:"updated_at"`
}

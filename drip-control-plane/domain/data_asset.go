package domain

import "time"

// DataAsset 数据资产领域模型
type DataAsset struct {
    ID               string     `json:"id"`
    TenantID         string     `json:"tenant_id"`
    Name             string     `json:"name"`
    Description      string     `json:"description"`
    Type             string     `json:"type"` // 数据库类型、文件系统等
    Location         string     `json:"location"`
    OwnerID          string     `json:"owner_id"`
    SensitivityScore int        `json:"sensitivity_score"` // 敏感度评分 (0-100)
    RiskLevel        string     `json:"risk_level"`        // HIGH, MEDIUM, LOW
    DataSize         int64      `json:"data_size"`         // 数据大小（字节）
    RecordCount      int64      `json:"record_count"`      // 记录数量
    LastScannedAt    *time.Time `json:"last_scanned_at"`
    CreatedAt        time.Time  `json:"created_at"`
    UpdatedAt        time.Time  `json:"updated_at"`
}

package domain

import "time"

// BackupRecord 备份记录领域模型
type BackupRecord struct {
	ID              string     `json:"id"`
	DataAssetID     string     `json:"data_asset_id"`
	TenantID        string     `json:"tenant_id"`
	BackupType      string     `json:"backup_type"` // FULL, INCREMENTAL, DIFFERENTIAL
	Status          string     `json:"status"`      // PENDING, IN_PROGRESS, SUCCESS, FAILED
	StartTime       time.Time  `json:"start_time"`
	EndTime         *time.Time `json:"end_time"`
	Duration        int64      `json:"duration"`         // 备份耗时（秒）
	BackupSize      int64      `json:"backup_size"`      // 备份大小（字节）
	StorageLocation string     `json:"storage_location"` // 备份存储位置
	ErrorMessage    string     `json:"error_message"`
	RetentionDays   int        `json:"retention_days"` // 保留天数
	CreatedAt       time.Time  `json:"created_at"`
	UpdatedAt       time.Time  `json:"updated_at"`
}

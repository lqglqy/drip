package domain

import "time"

// Job 任务领域模型
type Job struct {
	ID           string     `json:"id"`
	TenantID     string     `json:"tenant_id"`
	JobType      string     `json:"job_type"` // SCAN, BACKUP, RESTORE
	Name         string     `json:"name"`
	Description  string     `json:"description"`
	Status       string     `json:"status"`        // PENDING, RUNNING, SUCCESS, FAILED, CANCELLED
	TargetAssets []string   `json:"target_assets"` // 目标数据资产 ID 列表
	StartTime    *time.Time `json:"start_time"`
	EndTime      *time.Time `json:"end_time"`
	Progress     int        `json:"progress"` // 进度百分比 (0-100)
	CreatedBy    string     `json:"created_by"`
	ErrorMessage string     `json:"error_message"`
	RetryCount   int        `json:"retry_count"`
	MaxRetries   int        `json:"max_retries"`
	CreatedAt    time.Time  `json:"created_at"`
	UpdatedAt    time.Time  `json:"updated_at"`
}

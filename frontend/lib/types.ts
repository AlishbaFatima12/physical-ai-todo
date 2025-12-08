/**
 * TypeScript type definitions matching backend models
 */

export type Priority = 'low' | 'medium' | 'high'

export type ActionType = 'created' | 'updated' | 'completed' | 'deleted' | 'restored'

export interface Task {
  id: number
  title: string
  description?: string
  completed: boolean
  priority: Priority
  tags?: string
  display_order: number
  is_template: boolean
  created_at: string
  updated_at: string
  subtasks?: Subtask[]
  notes?: Note[]
  attachments?: Attachment[]
  activity_logs?: ActivityLog[]
}

export interface Subtask {
  id: number
  task_id: number
  title: string
  completed: boolean
  display_order: number
  created_at: string
  updated_at: string
}

export interface Note {
  id: number
  task_id: number
  content: string
  created_at: string
  updated_at: string
}

export interface Attachment {
  id: number
  task_id: number
  filename: string
  file_url: string
  file_size: number
  mime_type: string
  ocr_text?: string
  created_at: string
}

export interface Template {
  id: number
  name: string
  title: string
  description?: string
  priority: Priority
  tags?: string
  subtasks?: string
  created_at: string
  updated_at: string
}

export interface ActivityLog {
  id: number
  task_id: number
  action_type: ActionType
  field_changed?: string
  old_value?: string
  new_value?: string
  created_at: string
}

export interface VoiceCommand {
  id: number
  transcript: string
  language: string
  intent?: string
  confidence?: number
  created_at: string
}

export interface ChatMessage {
  id: number
  role: 'user' | 'assistant'
  content: string
  language: string
  created_at: string
}

// Request types
export interface TaskCreate {
  title: string
  description?: string
  priority?: Priority
  tags?: string
  display_order?: number
}

export interface TaskUpdate {
  title?: string
  description?: string
  completed?: boolean
  priority?: Priority
  tags?: string
  display_order?: number
}

export interface SubtaskCreate {
  title: string
  display_order?: number
}

export interface SubtaskUpdate {
  title?: string
  completed?: boolean
  display_order?: number
}

export interface NoteCreate {
  content: string
}

export interface BulkOperationRequest {
  task_ids: number[]
}

export interface BulkTagRequest extends BulkOperationRequest {
  tag: string
}

export interface BulkPriorityRequest extends BulkOperationRequest {
  priority: Priority
}

export interface ReorderItem {
  id: number
  display_order: number
}

export interface ReorderRequest {
  items: ReorderItem[]
}

// Filter and search types
export interface TaskFilters {
  completed?: boolean
  priority?: Priority
  tags?: string
  search?: string
  sort?: 'created_at' | 'updated_at' | 'priority' | 'title' | 'display_order'
  order?: 'asc' | 'desc'
  limit?: number
  offset?: number
}

// Analytics types
export interface AnalyticsSummary {
  total_tasks: number
  completed_tasks: number
  pending_tasks: number
  completion_rate: number
  tasks_by_priority: Record<Priority, number>
  tasks_by_tag: Record<string, number>
}

export interface ProductivityData {
  most_productive_day: string
  most_productive_hour: number
  avg_completion_time_hours: number
}

export interface TimelineDataPoint {
  date: string
  completed: number
  created: number
}

/**
 * TypeScript type definitions matching backend API schemas
 *
 * These types ensure type safety between frontend and backend.
 */

/**
 * Priority levels for tasks
 */
export type Priority = 'high' | 'medium' | 'low'

/**
 * Supported languages
 */
export type Language = 'en' | 'ur' | 'ar' | 'es' | 'fr' | 'de'

/**
 * Task entity (matches backend TaskRead schema)
 */
export interface Task {
  id: number
  title: string
  description: string
  completed: boolean
  priority: Priority
  tags: string[]
  created_at: string // ISO datetime string
  updated_at: string // ISO datetime string
}

/**
 * Task creation payload (matches backend TaskCreate schema)
 */
export interface TaskCreate {
  title: string
  description?: string
  priority?: Priority
  tags?: string[]
}

/**
 * Task full update payload (matches backend TaskUpdate schema)
 */
export interface TaskUpdate {
  title: string
  description: string
  priority: Priority
  tags: string[]
  completed: boolean
}

/**
 * Task partial update payload (matches backend TaskPatch schema)
 */
export interface TaskPatch {
  title?: string
  description?: string
  priority?: Priority
  tags?: string[]
  completed?: boolean
}

/**
 * Task list response (matches backend TaskListResponse schema)
 */
export interface TaskListResponse {
  tasks: Task[]
  total: number
  limit: number
  offset: number
}

/**
 * Voice command creation payload
 */
export interface VoiceCommandCreate {
  transcript: string
  language: Language
}

/**
 * Chat message creation payload
 */
export interface ChatMessageCreate {
  content: string
  language: Language
}

/**
 * Chat message entity
 */
export interface ChatMessage {
  id: number
  role: 'user' | 'assistant'
  content: string
  language: Language
  created_at: string
}

/**
 * API error response
 */
export interface APIError {
  error: string
  message: string
  details?: Record<string, any>
}

/**
 * Filter options for task list
 */
export interface TaskFilters {
  search?: string
  completed?: boolean
  priority?: Priority
  tags?: string
  sort?: 'created_at' | 'updated_at' | 'priority' | 'title'
  order?: 'asc' | 'desc'
  limit?: number
  offset?: number
}

/**
 * Voice recognition hook state
 */
export interface VoiceRecognitionState {
  transcript: string
  isListening: boolean
  error: string | null
  startListening: () => void
  stopListening: () => void
}

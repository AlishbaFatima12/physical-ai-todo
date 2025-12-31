/**
 * API client for backend communication
 */
import { Task, TaskCreate, TaskUpdate, TaskFilters, Notification } from './types'

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1'

/**
 * Custom error class for API errors
 */
export class APIError extends Error {
  constructor(
    message: string,
    public status?: number,
    public data?: any
  ) {
    super(message)
    this.name = 'APIError'
  }
}

/**
 * Generic fetch wrapper with error handling
 */
async function fetchAPI<T>(
  endpoint: string,
  options: RequestInit = {}
): Promise<T> {
  const url = `${API_BASE_URL}${endpoint}`

  const config: RequestInit = {
    ...options,
    credentials: 'include', // Include cookies for authentication
    headers: {
      'Content-Type': 'application/json',
      ...options.headers,
    },
  }

  try {
    const response = await fetch(url, config)

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}))
      throw new APIError(
        errorData.detail || `HTTP Error ${response.status}`,
        response.status,
        errorData
      )
    }

    // Handle 204 No Content
    if (response.status === 204) {
      return null as T
    }

    return await response.json()
  } catch (error) {
    if (error instanceof APIError) {
      throw error
    }
    throw new APIError(
      error instanceof Error ? error.message : 'Network error',
      undefined,
      error
    )
  }
}

/**
 * Build query string from filters
 */
function buildQueryString(filters?: TaskFilters): string {
  if (!filters) return ''

  const params = new URLSearchParams()

  Object.entries(filters).forEach(([key, value]) => {
    if (value !== undefined && value !== null) {
      params.append(key, String(value))
    }
  })

  const queryString = params.toString()
  return queryString ? `?${queryString}` : ''
}

/**
 * Trigger notification refresh (dispatches custom event)
 */
function refreshNotifications() {
  if (typeof window !== 'undefined') {
    window.dispatchEvent(new Event('refreshNotifications'))
  }
}

/**
 * API client methods
 */

// Individual named exports for direct import
export const getTasks = (filters?: TaskFilters) =>
  fetchAPI<{ tasks: Task[]; total: number; limit: number; offset: number }>(`/tasks${buildQueryString(filters)}`)

export const getTask = (id: number) =>
  fetchAPI<Task>(`/tasks/${id}`)

export const createTask = async (data: TaskCreate) => {
  const result = await fetchAPI<Task>('/tasks', {
    method: 'POST',
    body: JSON.stringify(data),
  })
  refreshNotifications() // Trigger notification refresh
  return result
}

export const updateTask = async (id: number, data: TaskUpdate) => {
  const result = await fetchAPI<Task>(`/tasks/${id}`, {
    method: 'PATCH',
    body: JSON.stringify(data),
  })
  refreshNotifications() // Trigger notification refresh
  return result
}

export const deleteTask = async (id: number) => {
  const result = await fetchAPI<void>(`/tasks/${id}`, {
    method: 'DELETE',
  })
  refreshNotifications() // Trigger notification refresh
  return result
}

export const toggleComplete = async (id: number) => {
  const result = await fetchAPI<Task>(`/tasks/${id}/toggle`, {
    method: 'POST',
  })
  refreshNotifications() // Trigger notification refresh
  return result
}

// Notification API functions
export const getNotifications = (filters?: { is_read?: boolean; type?: string; limit?: number; offset?: number }) =>
  fetchAPI<Notification[]>(`/notifications${buildQueryString(filters)}`)

export const getUnreadCount = () =>
  fetchAPI<{ unread_count: number }>('/notifications/unread-count')

export const markNotificationAsRead = (id: number) =>
  fetchAPI<Notification>(`/notifications/${id}`, {
    method: 'PATCH',
  })

export const markAllNotificationsAsRead = () =>
  fetchAPI<{ success: boolean; updated_count: number; message: string }>('/notifications/mark-all-read', {
    method: 'POST',
  })

export const deleteNotification = (id: number) =>
  fetchAPI<void>(`/notifications/${id}`, {
    method: 'DELETE',
  })

// Grouped API object for convenience
export const api = {
  getTasks,
  getTask,
  createTask,
  updateTask,
  deleteTask,
  toggleComplete,
  // Health check
  healthCheck: () =>
    fetchAPI<{ status: string; version: string; service: string }>('/health'),
}

export default api

'use client'

import { Task, Priority } from '@/lib/types'
import { toggleComplete, deleteTask } from '@/lib/api'
import { useState } from 'react'

interface TaskItemProps {
  task: Task
  onUpdate: () => void
  onEdit: (task: Task) => void
}

const priorityColors: Record<Priority, string> = {
  high: 'bg-red-100 text-red-800 border-red-300',
  medium: 'bg-yellow-100 text-yellow-800 border-yellow-300',
  low: 'bg-blue-100 text-blue-800 border-blue-300',
}

const priorityLabels: Record<Priority, string> = {
  high: 'High Priority',
  medium: 'Medium',
  low: 'Low',
}

export default function TaskItem({ task, onUpdate, onEdit }: TaskItemProps) {
  const [isDeleting, setIsDeleting] = useState(false)
  const [isToggling, setIsToggling] = useState(false)

  const handleToggle = async () => {
    if (isToggling) return
    setIsToggling(true)
    try {
      await toggleComplete(task.id)
      onUpdate()
    } catch (error) {
      console.error('Failed to toggle task:', error)
      alert('Failed to update task')
    } finally {
      setIsToggling(false)
    }
  }

  const handleDelete = async () => {
    if (isDeleting) return
    if (!confirm('Are you sure you want to delete this task?')) return

    setIsDeleting(true)
    try {
      await deleteTask(task.id)
      onUpdate()
    } catch (error) {
      console.error('Failed to delete task:', error)
      alert('Failed to delete task')
    } finally {
      setIsDeleting(false)
    }
  }

  const formatDate = (dateString: string) => {
    const date = new Date(dateString)
    return date.toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
    })
  }

  return (
    <div
      className={`bg-white rounded-lg shadow-md p-4 transition-all duration-300 hover:shadow-lg border-l-4 ${
        task.completed ? 'border-green-500 opacity-75' : 'border-blue-500'
      }`}
    >
      <div className="flex items-start gap-3">
        {/* Checkbox */}
        <button
          onClick={handleToggle}
          disabled={isToggling}
          className="flex-shrink-0 mt-1"
        >
          <div
            className={`w-6 h-6 rounded border-2 flex items-center justify-center transition-all ${
              task.completed
                ? 'bg-green-500 border-green-500'
                : 'border-gray-300 hover:border-green-400'
            } ${isToggling ? 'opacity-50' : ''}`}
          >
            {task.completed && (
              <svg className="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
              </svg>
            )}
          </div>
        </button>

        {/* Task Content */}
        <div className="flex-grow min-w-0">
          {/* Title and Priority */}
          <div className="flex items-start gap-2 flex-wrap mb-1">
            <h3
              className={`text-lg font-semibold ${
                task.completed ? 'line-through text-gray-500' : 'text-gray-900'
              }`}
            >
              {task.title}
            </h3>
            <span
              className={`inline-flex items-center px-2 py-1 rounded-full text-xs font-medium border ${
                priorityColors[task.priority]
              }`}
            >
              {priorityLabels[task.priority]}
            </span>
          </div>

          {/* Description */}
          {task.description && (
            <p className={`text-sm mb-2 ${task.completed ? 'text-gray-400' : 'text-gray-600'}`}>
              {task.description}
            </p>
          )}

          {/* Tags */}
          {task.tags && task.tags.length > 0 && (
            <div className="flex flex-wrap gap-1 mb-2">
              {task.tags.map((tag, index) => (
                <span
                  key={index}
                  className="inline-flex items-center px-2 py-1 rounded-full text-xs bg-gray-100 text-gray-700"
                >
                  #{tag}
                </span>
              ))}
            </div>
          )}

          {/* Dates */}
          <div className="flex flex-wrap gap-3 text-xs text-gray-500 mb-2">
            <span title="Created">
              Created: {formatDate(task.created_at)}
            </span>
            {task.updated_at !== task.created_at && (
              <span title="Last Updated">
                Updated: {formatDate(task.updated_at)}
              </span>
            )}
          </div>

          {/* Actions */}
          <div className="flex gap-2 mt-2">
            <button
              onClick={() => onEdit(task)}
              className="px-3 py-1 text-sm bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors"
            >
              Edit
            </button>
            <button
              onClick={handleDelete}
              disabled={isDeleting}
              className="px-3 py-1 text-sm bg-red-500 text-white rounded hover:bg-red-600 transition-colors disabled:opacity-50"
            >
              {isDeleting ? 'Deleting...' : 'Delete'}
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}

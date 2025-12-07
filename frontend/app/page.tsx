'use client'

import { useState, useEffect } from 'react'
import { Task } from '@/lib/types'
import { fetchTasks } from '@/lib/api'
import TaskList from '@/components/TaskList'
import TaskForm from '@/components/TaskForm'

export default function Home() {
  const [tasks, setTasks] = useState<Task[]>([])
  const [isLoading, setIsLoading] = useState(true)
  const [editingTask, setEditingTask] = useState<Task | null>(null)
  const [showForm, setShowForm] = useState(false)
  const [stats, setStats] = useState({ total: 0, completed: 0, pending: 0 })

  const loadTasks = async () => {
    try {
      setIsLoading(true)
      const response = await fetchTasks()
      setTasks(response.tasks)

      // Calculate stats
      const completed = response.tasks.filter(t => t.completed).length
      setStats({
        total: response.tasks.length,
        completed,
        pending: response.tasks.length - completed,
      })
    } catch (error) {
      console.error('Failed to load tasks:', error)
      alert('Failed to load tasks. Make sure the backend is running.')
    } finally {
      setIsLoading(false)
    }
  }

  useEffect(() => {
    loadTasks()
  }, [])

  const handleTaskCreated = () => {
    setShowForm(false)
    setEditingTask(null)
    loadTasks()
  }

  const handleEdit = (task: Task) => {
    setEditingTask(task)
    setShowForm(true)
  }

  const handleCancel = () => {
    setEditingTask(null)
    setShowForm(false)
  }

  return (
    <main className="min-h-screen animated-gradient py-8 px-4">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-5xl font-bold text-white mb-2 drop-shadow-lg">
            Physical AI Todo
          </h1>
          <p className="text-white text-lg opacity-90">
            Modern Task Management with Interactive Features
          </p>
        </div>

        {/* Stats Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
          <div className="bg-white bg-opacity-20 backdrop-blur-lg rounded-xl p-4 text-white">
            <div className="text-3xl font-bold">{stats.total}</div>
            <div className="text-sm opacity-90">Total Tasks</div>
          </div>
          <div className="bg-white bg-opacity-20 backdrop-blur-lg rounded-xl p-4 text-white">
            <div className="text-3xl font-bold">{stats.pending}</div>
            <div className="text-sm opacity-90">Pending</div>
          </div>
          <div className="bg-white bg-opacity-20 backdrop-blur-lg rounded-xl p-4 text-white">
            <div className="text-3xl font-bold">{stats.completed}</div>
            <div className="text-sm opacity-90">Completed</div>
          </div>
        </div>

        {/* Add Task Button */}
        {!showForm && (
          <div className="mb-6 text-center">
            <button
              onClick={() => setShowForm(true)}
              className="px-8 py-4 bg-white text-purple-600 rounded-xl font-bold text-lg hover:bg-opacity-90 transition-all transform hover:scale-105 active:scale-95 shadow-xl"
            >
              + Create New Task
            </button>
          </div>
        )}

        {/* Task Form */}
        {showForm && (
          <TaskForm
            onSuccess={handleTaskCreated}
            onCancel={handleCancel}
            editingTask={editingTask}
          />
        )}

        {/* Task List */}
        <div className="bg-white bg-opacity-10 backdrop-blur-lg rounded-xl p-6">
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-2xl font-bold text-white">Your Tasks</h2>
            <button
              onClick={loadTasks}
              className="px-4 py-2 bg-white bg-opacity-20 text-white rounded-lg hover:bg-opacity-30 transition-colors"
              title="Refresh tasks"
            >
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
              </svg>
            </button>
          </div>

          <TaskList
            tasks={tasks}
            isLoading={isLoading}
            onUpdate={loadTasks}
            onEdit={handleEdit}
          />
        </div>

        {/* Footer */}
        <div className="text-center mt-8 text-white opacity-75">
          <p className="text-sm">
            Built with Next.js, FastAPI, and Neon DB
          </p>
          <p className="text-xs mt-1">
            Phase II - Full-Stack Web Application
          </p>
        </div>
      </div>
    </main>
  )
}

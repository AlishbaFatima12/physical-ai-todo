'use client'

import { useState } from 'react'
import { useQuery } from '@tanstack/react-query'
import { getTasks } from '@/lib/api'
import TaskForm from '@/components/TaskForm'
import TaskList from '@/components/TaskList'
import { Task } from '@/lib/types'

export default function Home() {
  const [editingTask, setEditingTask] = useState<Task | null>(null)
  const [showForm, setShowForm] = useState(false)

  // Fetch tasks using React Query
  const { data, isLoading, refetch } = useQuery({
    queryKey: ['tasks'],
    queryFn: () => getTasks(),
  })

  const tasks = data?.tasks || []

  const handleSuccess = () => {
    refetch()
    setShowForm(false)
    setEditingTask(null)
  }

  const handleEdit = (task: Task) => {
    setEditingTask(task)
    setShowForm(true)
  }

  const handleCancel = () => {
    setShowForm(false)
    setEditingTask(null)
  }

  return (
    <main className="min-h-screen bg-gradient-to-br from-blue-600 via-purple-600 to-pink-500 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-5xl font-bold text-white mb-2">
            Physical AI Todo
          </h1>
          <p className="text-white text-opacity-90">
            Your intelligent task management system
          </p>
        </div>

        {/* Stats Card */}
        <div className="bg-white bg-opacity-20 backdrop-blur-lg rounded-xl p-6 mb-6 shadow-xl">
          <div className="grid grid-cols-3 gap-4 text-center">
            <div>
              <div className="text-3xl font-bold text-white">{tasks.length}</div>
              <div className="text-white text-opacity-75 text-sm">Total</div>
            </div>
            <div>
              <div className="text-3xl font-bold text-white">
                {tasks.filter((t) => !t.completed).length}
              </div>
              <div className="text-white text-opacity-75 text-sm">Active</div>
            </div>
            <div>
              <div className="text-3xl font-bold text-white">
                {tasks.filter((t) => t.completed).length}
              </div>
              <div className="text-white text-opacity-75 text-sm">Completed</div>
            </div>
          </div>
        </div>

        {/* Task Form */}
        {showForm ? (
          <TaskForm
            onSuccess={handleSuccess}
            onCancel={handleCancel}
            editingTask={editingTask}
          />
        ) : (
          <button
            onClick={() => setShowForm(true)}
            className="w-full bg-white rounded-xl shadow-xl p-6 mb-6 hover:shadow-2xl transition-shadow"
          >
            <div className="flex items-center justify-center gap-2">
              <svg
                className="w-6 h-6 text-blue-500"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M12 4v16m8-8H4"
                />
              </svg>
              <span className="text-xl font-semibold text-gray-700">
                Create New Task
              </span>
            </div>
          </button>
        )}

        {/* Task List */}
        <div className="bg-white bg-opacity-10 backdrop-blur-lg rounded-xl p-6 shadow-xl">
          <h2 className="text-2xl font-bold text-white mb-4">Your Tasks</h2>
          <TaskList
            tasks={tasks}
            isLoading={isLoading}
            onUpdate={refetch}
            onEdit={handleEdit}
          />
        </div>

        {/* Footer */}
        <div className="mt-8 text-center text-white text-opacity-75 text-sm">
          <p>
            Backend: <code className="bg-white bg-opacity-20 px-2 py-1 rounded">
              http://localhost:8000
            </code>
          </p>
        </div>
      </div>
    </main>
  )
}

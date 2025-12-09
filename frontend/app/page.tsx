'use client'

import { useState } from 'react'
import { useQuery } from '@tanstack/react-query'
import { getTasks } from '@/lib/api'
import TaskForm from '@/components/TaskForm'
import TaskList from '@/components/TaskList'
import FilterBar from '@/components/FilterBar'
import ThemeToggle from '@/components/ThemeToggle'
import { Task } from '@/lib/types'

export default function Home() {
  const [editingTask, setEditingTask] = useState<Task | null>(null)
  const [showForm, setShowForm] = useState(false)

  // Filter/Search/Sort state
  const [search, setSearch] = useState('')
  const [priority, setPriority] = useState('')
  const [completed, setCompleted] = useState('all')
  const [tags, setTags] = useState('')
  const [sortField, setSortField] = useState('created_at')
  const [sortOrder, setSortOrder] = useState('desc')

  // Fetch tasks using React Query with filters
  const { data, isLoading, refetch } = useQuery({
    queryKey: ['tasks', search, priority, completed, tags, sortField, sortOrder],
    queryFn: () => getTasks({
      search: search || undefined,
      priority: priority || undefined,
      completed: completed === 'all' ? undefined : completed === 'true',
      tags: tags || undefined,
      sort: sortField,
      order: sortOrder,
    }),
  })

  const tasks = data?.tasks || []

  const handleClearFilters = () => {
    setSearch('')
    setPriority('')
    setCompleted('all')
    setTags('')
    setSortField('created_at')
    setSortOrder('desc')
  }

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
    <main className="min-h-screen bg-gradient-to-br from-blue-600 via-purple-600 to-pink-500 dark:from-gray-900 dark:via-blue-900 dark:to-purple-900 py-12 px-4 sm:px-6 lg:px-8 transition-colors duration-200">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="flex items-center justify-between mb-8">
          <div className="text-center flex-grow">
            <h1 className="text-5xl font-bold text-white mb-2">
              FlowTask
            </h1>
            <p className="text-white text-opacity-90">
              Effortless Productivity, Beautiful Design
            </p>
          </div>
          <div className="absolute top-6 right-6">
            <ThemeToggle />
          </div>
        </div>

        {/* Stats Card */}
        <div className="bg-white bg-opacity-20 backdrop-blur-lg rounded-xl p-6 mb-6 shadow-xl">
          <div className="grid grid-cols-3 gap-4 text-center">
            <div>
              <div className="text-3xl font-bold text-white">{data?.total || 0}</div>
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

        {/* FilterBar */}
        <FilterBar
          search={search}
          onSearchChange={setSearch}
          priority={priority}
          onPriorityChange={setPriority}
          completed={completed}
          onCompletedChange={setCompleted}
          tags={tags}
          onTagsChange={setTags}
          sortField={sortField}
          onSortFieldChange={setSortField}
          sortOrder={sortOrder}
          onSortOrderChange={setSortOrder}
          onClearFilters={handleClearFilters}
        />

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

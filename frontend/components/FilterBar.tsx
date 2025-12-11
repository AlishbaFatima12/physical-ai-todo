'use client'

import { Priority } from '@/lib/types'

interface FilterBarProps {
  search: string
  onSearchChange: (value: string) => void
  priority: string
  onPriorityChange: (value: string) => void
  completed: string
  onCompletedChange: (value: string) => void
  sortField: string
  onSortFieldChange: (value: string) => void
  sortOrder: string
  onSortOrderChange: (value: string) => void
  tags: string
  onTagsChange: (value: string) => void
  onClearFilters: () => void
}

export default function FilterBar({
  search,
  onSearchChange,
  priority,
  onPriorityChange,
  completed,
  onCompletedChange,
  sortField,
  onSortFieldChange,
  sortOrder,
  onSortOrderChange,
  tags,
  onTagsChange,
  onClearFilters,
}: FilterBarProps) {
  const hasActiveFilters = search || priority || completed !== 'all' || tags

  return (
    <div className="bg-white bg-opacity-10 backdrop-blur-lg rounded-xl p-6 mb-6 shadow-xl">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-xl font-semibold text-white">Filters & Search</h3>
        {hasActiveFilters && (
          <button
            onClick={onClearFilters}
            className="text-sm text-white bg-white bg-opacity-20 px-3 py-1 rounded-lg hover:bg-opacity-30 transition-colors"
          >
            Clear All
          </button>
        )}
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {/* Search */}
        <div>
          <label className="block text-sm font-medium text-white mb-1">
            Search
          </label>
          <input
            type="text"
            value={search}
            onChange={(e) => onSearchChange(e.target.value)}
            placeholder="Search tasks..."
            className="w-full px-4 py-2 rounded-lg border border-white border-opacity-20 bg-white bg-opacity-10 text-white placeholder-white placeholder-opacity-50 focus:ring-2 focus:ring-white focus:ring-opacity-50 outline-none"
          />
        </div>

        {/* Priority Filter */}
        <div>
          <label className="block text-sm font-medium text-white mb-1">
            Priority
          </label>
          <select
            value={priority}
            onChange={(e) => onPriorityChange(e.target.value)}
            className="w-full px-4 py-2 rounded-lg border border-white border-opacity-20 bg-white bg-opacity-10 text-white focus:ring-2 focus:ring-white focus:ring-opacity-50 outline-none"
          >
            <option value="" className="text-gray-900">All Priorities</option>
            <option value="high" className="text-gray-900">High Priority</option>
            <option value="medium" className="text-gray-900">Medium Priority</option>
            <option value="low" className="text-gray-900">Low Priority</option>
          </select>
        </div>

        {/* Completion Status */}
        <div>
          <label className="block text-sm font-medium text-white mb-1">
            Status
          </label>
          <select
            value={completed}
            onChange={(e) => onCompletedChange(e.target.value)}
            className="w-full px-4 py-2 rounded-lg border border-white border-opacity-20 bg-white bg-opacity-10 text-white focus:ring-2 focus:ring-white focus:ring-opacity-50 outline-none"
          >
            <option value="all" className="text-gray-900">All Tasks</option>
            <option value="false" className="text-gray-900">Active Only</option>
            <option value="true" className="text-gray-900">Completed Only</option>
          </select>
        </div>

        {/* Tags Filter */}
        <div>
          <label className="block text-sm font-medium text-white mb-1">
            Tags
          </label>
          <input
            type="text"
            value={tags}
            onChange={(e) => onTagsChange(e.target.value)}
            placeholder="work,urgent (comma-separated)"
            className="w-full px-4 py-2 rounded-lg border border-white border-opacity-20 bg-white bg-opacity-10 text-white placeholder-white placeholder-opacity-50 focus:ring-2 focus:ring-white focus:ring-opacity-50 outline-none"
          />
        </div>

        {/* Sort Field */}
        <div>
          <label className="block text-sm font-medium text-white mb-1">
            Sort By
          </label>
          <select
            value={sortField}
            onChange={(e) => onSortFieldChange(e.target.value)}
            className="w-full px-4 py-2 rounded-lg border border-white border-opacity-20 bg-white bg-opacity-10 text-white focus:ring-2 focus:ring-white focus:ring-opacity-50 outline-none"
          >
            <option value="created_at" className="text-gray-900">Date Created</option>
            <option value="updated_at" className="text-gray-900">Date Updated</option>
            <option value="priority" className="text-gray-900">Priority</option>
            <option value="title" className="text-gray-900">Title (A-Z)</option>
          </select>
        </div>

        {/* Sort Order */}
        <div>
          <label className="block text-sm font-medium text-white mb-1">
            Order
          </label>
          <select
            value={sortOrder}
            onChange={(e) => onSortOrderChange(e.target.value)}
            className="w-full px-4 py-2 rounded-lg border border-white border-opacity-20 bg-white bg-opacity-10 text-white focus:ring-2 focus:ring-white focus:ring-opacity-50 outline-none"
          >
            <option value="desc" className="text-gray-900">Descending</option>
            <option value="asc" className="text-gray-900">Ascending</option>
          </select>
        </div>
      </div>
    </div>
  )
}

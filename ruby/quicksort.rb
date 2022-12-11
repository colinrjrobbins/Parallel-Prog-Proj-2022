class QuickSort
  def quicksort(arr, first, last, sorter)
    if first < last
      p_index = partition(arr, first, last, sorter)
      quicksort(arr, first, p_index - 1, sorter)
      quicksort(arr, p_index + 1, last, sorter)
    end

    arr
  end

  def partition(arr, first, last, sorter)
    sorter_element = sorter.to_sym
    pivot = arr[last]
    p_index = first
    i = first

    while i < last
      if arr[i][sorter_element] < pivot[sorter_element]
        temp = arr[i]
        arr[i] = arr[p_index]
        arr[p_index] = temp
        p_index += 1
      elsif arr[i][sorter_element] == pivot[sorter_element]
        if arr[i][:first_name] < pivot[:first_name]
          temp = arr[i]
          arr[i] = arr[p_index]
          arr[p_index] = temp
          p_index += 1
        end
      end
      i += 1
    end
    temp = arr[p_index]
    arr[p_index] = pivot
    arr[last] = temp
    return p_index
  end
end
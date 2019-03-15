def best_store_by_total_sales(weekly_sales):
    """
    >>> best_store_by_total_sales([
    ...     [10, 10, 10, 10, 10, 10, 10],
    ...     [1, 1, 1, 1, 1, 1, 1],
    ...     [1, 1, 1, 1, 1],
    ...     []
    ... ])
    [0]

    >>> best_store_by_total_sales([
    ...     [10, 10, 10, 10, 10, 10, 10],
    ...     [1, 1, 1, 1, 1, 1, 1],
    ...     [10, 10, 10, 10, 10, 10, 10],
    ...     [1, 1, 1, 1, 1],
    ...     []
    ... ])
    [0, 2]

    >>> best_store_by_total_sales([])
    []
    """

    best_total_sales = 0;
    for store_sales in weekly_sales:
        store_total_sales = sum(store_sales)
        if store_total_sales > best_total_sales:
            best_total_sales = store_total_sales

    result = []
    for i, store_sales in enumerate(weekly_sales):
        if sum(store_sales) == best_total_sales:
            result.append(i)

    return result


def best_store_by_average_sales(weekly_sales):
    """
    >>> best_store_by_average_sales([
    ...     [10, 10, 10, 10, 10, 10, 10],
    ...     [1, 1, 1, 1, 1, 1, 1],
    ...     [1, 1, 1, 1, 1],
    ...     []
    ... ])
    [0]

    >>> best_store_by_average_sales([
    ...     [10, 10, 10, 10, 10, 10, 10],
    ...     [1, 1, 1, 1, 1, 1, 1],
    ...     [10, 10, 10, 10, 10, 10, 10],
    ...     [1, 1, 1, 1, 1],
    ...     []
    ... ])
    [0, 2]

    >>> best_store_by_average_sales([
    ...    [10, 10, 10, 10, 10, 10, 10],
    ...    [1, 1, 1, 1, 1, 1, 1],
    ...    [10, 10, 10, (10 + 10), (10 + 10)],
    ...    [1, 1, 1, 1, 1],
    ...    []
    ... ])
    [2]

    >>> best_store_by_average_sales([])
    []
    """

    best_average_sales = 0;
    for store_sales in weekly_sales:
        if len(store_sales) == 0:
            continue
        store_average_sales = sum(store_sales) / len(store_sales)
        if store_average_sales > best_average_sales:
            best_average_sales = store_average_sales

    result = []
    for i, store_sales in enumerate(weekly_sales):
        if len(store_sales) == 0:
            continue
        store_average_sales = sum(store_sales) / len(store_sales)
        if store_average_sales == best_average_sales:
            result.append(i)

    return result


def store_with_best_daily_sales(weekly_sales):
    """
    >>> store_with_best_daily_sales([
    ...     [10, 1, 1, 1, 1, 1, 1],
    ...     [1, 1, 1, 1, 1, 1, 1],
    ...     [1, 1, 1, 1, 1],
    ...     []
    ... ])
    [0]

    >>> store_with_best_daily_sales([
    ...     [10, 1, 1, 1, 1, 1, 1],
    ...     [1, 1, 1, 1, 1, 1, 1],
    ...     [10, 1, 1, 1, 1],
    ...     []
    ... ])
    [0, 2]

    >>> store_with_best_daily_sales([])
    []
    """

    best_daily_sales = 0;
    for store_sales in weekly_sales:
        if len(store_sales) == 0:
            continue
        store_sales.sort(reverse = True)
        best_store_daily_sales = store_sales[0]
        if best_store_daily_sales > best_daily_sales:
            best_daily_sales = best_store_daily_sales

    result = []
    for i, store_sales in enumerate(weekly_sales):
        if len(store_sales) == 0:
            continue
        store_sales.sort(reverse = True)
        best_store_daily_sales = store_sales[0]
        if best_store_daily_sales == best_daily_sales:
            result.append(i)

    return result


def store_with_worst_daily_sales(weekly_sales):
    """
    >>> store_with_worst_daily_sales([
    ...     [1, 1, 1, 1, 1, 1, 1],
    ...     [1, 1, 1, 1, 1],
    ...     [0, 1, 1, 1, 1],
    ...     []
    ... ])
    [2]

    >>> store_with_worst_daily_sales([
    ...    [0, 1, 1, 1, 1, 1, 1],
    ...    [1, 1, 1, 1, 1, 1, 1],
    ...    [0, 1, 1, 1, 1],
    ...    []
    ... ])
    [0, 2]

    >>> store_with_worst_daily_sales([])
    []
    """

    worst_daily_sales = float("inf");
    for store_sales in weekly_sales:
        if len(store_sales) == 0:
            continue
        store_sales.sort()
        worst_store_daily_sales = store_sales[0]
        if worst_store_daily_sales < worst_daily_sales:
            worst_daily_sales = worst_store_daily_sales

    result = []
    for i, store_sales in enumerate(weekly_sales):
        if len(store_sales) == 0:
            continue
        store_sales.sort()
        worst_store_daily_sales = store_sales[0]
        if worst_store_daily_sales == worst_daily_sales:
            result.append(i)

    return result


def top_3_store_sales(weekly_sales):
    """
    >>> top_3_store_sales([
    ...     [1000, 100, 10, 1, 1, 1, 1],
    ...     [1, 1, 10, 1, 100, 1, 1000],
    ...     [1, 1, 10, 1, 100],
    ...     []
    ... ])
    [[1000, 100, 10], [1000, 100, 10], [100, 10, 1], []]

    >>> top_3_store_sales([])
    []
    """

    top_sales = []
    top_to_show = 3

    for store_sales in weekly_sales:
        store_sales.sort(reverse = True)
        top_store_sales = store_sales[:top_to_show]
        top_sales.append(top_store_sales)

    return top_sales

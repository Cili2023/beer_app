class FilterMixin:
    def get_ordered_queryset(self, qs, initial_order):
        order_by = self.request.query_params.get('order')
        if not order_by:
            order_by = initial_order
        if qs:
            return qs.order_by(order_by)
        return []

    def filter_queryset(self, queryset, **kwargs):
        filters = []
        for k, vals in self.request.GET.lists():
            if k == 'range' and len(vals) > 0:
                filters['date__range'] = vals[0].split(',')
            if k not in self.excluded_params:
                filters[k] = vals[0] == 'true' if (k == 'active') else vals[0]

        filters.pop('order', None)
        filters.pop('serializer', None)

        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)

        return queryset.filter(**filters, **kwargs)

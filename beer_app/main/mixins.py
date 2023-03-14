from django.db.models import QuerySet


class FilterListMixin:
    excluded_params = [
        'search',
        'page'
    ]

    class Meta:
        abstract = True

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
        return queryset

    def get_ordered_queryset(self, qs, initial_order):
        order_by = self.request.query_params.get('order')
        if not order_by:
            order_by = initial_order
        if qs:
            return qs.order_by(order_by)
        return []

    def filter_queryset(self, queryset, **kwargs):
        filters = {}
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


class PaginatedListFilterMixin(FilterListMixin):

    def get_ordered_queryset(self, qs, initial_order):
        order_by = self.request.query_params.get('order')
        if not order_by:
            order_by = initial_order
        if order_by not in self.special_order_fields:
            from django.db.models.functions import Lower

            if order_by.startswith('-'):
                if '' in order_by:
                    return sorted(qs.order_by(Lower(order_by[1:])), key=lambda x: qs.filter(id=x.id).values_list(
                        order_by[1:])[0][0].lower(), reverse=True
                    )
                return sorted(qs.order_by(Lower(order_by[1:])), key=lambda x: x.dict__[order_by[1:]].lower(), reverse=True)
            return qs.order_by(Lower(order_by))
        return qs.order_by(order_by)

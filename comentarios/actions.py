def reprova_comentarios(modeladmin, request, queryset):
    queryset.update(aprovado=False)


def aprova_comentarios(modelsadmin, request, queryset):
    queryset.update(aprovado=True)


reprova_comentarios.short_description = 'Reprovar comentário'
aprova_comentarios.short_description = 'Aprovar comentário'
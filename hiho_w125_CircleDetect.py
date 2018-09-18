# DFS(x):
#     color[x] = GREY
#     FOR y : g[x] # x->y是一条边
#         IF color[y] == GREY
#             EXIT(CIRCLE_FOUND)
#         IF color[y] == WHITE
#             DFS(y)
#     color[x] = BLACK
# MAIN:
#     FOR x = 1 .. N:
#         IF color[x] == WHITE:
#             DFS(x)
#     EXIT(CIRCLE_NOT_FOUND)


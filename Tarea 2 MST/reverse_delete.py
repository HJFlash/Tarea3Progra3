import time
inicio = time.time()
class Graph:
	def __init__(self, v):

		# No. of vertices
		self.v = v
		self.adj = [0] * v
		self.edges = []
		for i in range(v):
			self.adj[i] = []

	# function to add an edge to graph
	def addEdge(self, u: int, v: int, w: int):
		self.adj[u].append(v) # Add w to v’s list.
		self.adj[v].append(u) # Add w to v’s list.
		self.edges.append((w, (u, v)))

	def dfs(self, v: int, visited: list):

		# Mark the current node as visited and print it
		visited[v] = True

		# Recur for all the vertices adjacent to
		# this vertex
		for i in self.adj[v]:
			if not visited[i]:
				self.dfs(i, visited)

	# Returns true if graph is connected
	# Returns true if given graph is connected, else false
	def connected(self):
		visited = [False] * self.v

		# Find all reachable vertices from first vertex
		self.dfs(0, visited)

		# If set of reachable vertices includes all,
		# return true.
		for i in range(1, self.v):
			if not visited[i]:
				return False

		return True

	# This function assumes that edge (u, v)
	# exists in graph or not,
	def reverseDeleteMST(self):

		# Sort edges in increasing order on basis of cost
		self.edges.sort(key = lambda a: a[0])

		mst_wt = 0 # Initialize weight of MST

		print("Edges in MST")

		# Iterate through all sorted edges in
		# decreasing order of weights
		for i in range(len(self.edges) - 1, -1, -1):
			u = self.edges[i][1][0]
			v = self.edges[i][1][1]

			# Remove edge from undirected graph
			self.adj[u].remove(v)
			self.adj[v].remove(u)

			# Adding the edge back if removing it
			# causes disconnection. In this case this
			# edge becomes part of MST.
			if self.connected() == False:
				self.adj[u].append(v)
				self.adj[v].append(u)

				# This edge is part of MST
				print("( %d, %d )" % (u, v))
				mst_wt += self.edges[i][0]
		print("Total weight of MST is", mst_wt)

# Driver Code


# create the graph given in above figure
V = 80
g = Graph(V)

	# making above shown graph
edges = [
    (10, 65, 644),
    (3, 68, 355),
    (35, 39, 91),
    (59, 11, 808),
    (48, 26, 140),
    (56, 48, 326),
    (5, 41, 412),
    (71, 50, 159),
    (31, 74, 889),
    (74, 64, 410),
    (2, 7, 440),
    (55, 42, 92),
    (14, 3, 203),
    (35, 77, 767),
    (60, 66, 606),
    (26, 35, 696),
    (71, 23, 783),
    (12, 22, 372),
    (22, 71, 155),
    (65, 42, 18),
    (6, 25, 907),
    (61, 30, 300),
    (77, 6, 218),
    (0, 28, 139),
    (28, 74, 458),
    (38, 44, 405),
    (33, 57, 570),
    (38, 56, 755),
    (27, 18, 168),
    (3, 12, 133),
    (21, 49, 79),
    (46, 73, 111),
    (58, 26, 463),
    (64, 63, 254),
    (19, 8, 702),
    (63, 61, 310),
    (56, 37, 397),
    (23, 70, 887),
    (17, 60, 154),
    (44, 62, 105),
    (35, 65, 497),
    (67, 76, 191),
    (62, 4, 704),
    (78, 47, 146),
    (15, 16, 615),
    (65, 47, 440),
    (2, 61, 394),
    (14, 40, 73),
    (32, 16, 699),
    (67, 24, 345),
    (69, 0, 926),
    (37, 57, 541),
    (29, 50, 934),
    (58, 31, 986),
    (36, 73, 270),
    (25, 24, 231),
    (36, 33, 46),
    (58, 71, 238),
    (15, 77, 507),
    (52, 17, 602),
    (55, 59, 787),
    (17, 1, 11),
    (71, 20, 603),
    (50, 6, 154),
    (65, 29, 962),
    (18, 39, 697),
    (14, 66, 382),
    (1, 11, 671),
    (5, 24, 98),
    (24, 63, 527),
    (64, 44, 991),
    (78, 12, 238),
    (16, 23, 962),
    (20, 3, 463),
    (52, 36, 830),
    (48, 12, 119),
    (12, 59, 3),
    (33, 12, 154),
    (37, 22, 864),
    (18, 30, 742),
    (24, 36, 996),
    (43, 30, 301),
    (57, 21, 939),
    (37, 22, 435),
    (78, 58, 525),
    (10, 58, 362),
    (39, 30, 981),
    (14, 76, 753),
    (27, 15, 196),
    (66, 38, 563),
    (32, 31, 857),
    (29, 15, 215),
    (62, 29, 771),
    (67, 46, 398),
    (78, 43, 19),
    (57, 53, 302),
    (47, 63, 359),
    (12, 36, 525),
    (68, 46, 918),
    (12, 62, 205),
    (47, 32, 748),
    (55, 78, 540),
    (68, 20, 11),
    (44, 62, 975),
    (12, 14, 105),
    (30, 50, 125),
    (78, 24, 969),
    (42, 30, 182),
    (25, 54, 620),
    (40, 72, 767),
    (1, 79, 221),
    (14, 42, 137),
    (26, 13, 82),
    (37, 7, 170),
    (78, 24, 797),
    (75, 49, 938),
    (14, 60, 862),
    (52, 33, 715),
    (57, 8, 269),
    (48, 3, 502),
    (11, 32, 148),
    (58, 14, 583),
    (54, 70, 465),
    (36, 44, 836),
    (57, 68, 186),
    (74, 69, 42),
    (11, 64, 242),
    (49, 67, 943),
    (79, 75, 932),
    (28, 17, 314),
    (76, 55, 929),
    (10, 31, 131),
    (78, 33, 762),
    (27, 46, 330),
    (8, 14, 579),
    (41, 68, 23),
    (26, 10, 54),
    (65, 29, 838),
    (61, 67, 497),
    (53, 13, 448),
    (8, 63, 1000),
    (35, 58, 912),
    (54, 0, 206),
    (6, 54, 822),
    (49, 19, 112),
    (6, 8, 762),
    (14, 2, 339),
    (77, 21, 663),
    (47, 75, 888),
    (40, 70, 29),
    (23, 73, 899),
    (24, 25, 341),
    (54, 11, 677),
    (53, 15, 154),
    (23, 40, 452),
    (17, 65, 444),
    (21, 79, 690),
    (7, 57, 256),
    (34, 64, 42),
    (74, 48, 563),
    (36, 8, 125),
    (39, 30, 180),
    (70, 73, 739),
    (23, 18, 688),
    (15, 31, 367),
    (72, 45, 973),
    (25, 18, 440),
    (51, 24, 690),
    (11, 60, 788),
    (50, 73, 759),
    (0, 43, 76),
    (37, 75, 684),
    (77, 35, 354),
    (22, 35, 926),
    (79, 33, 995),
    (49, 51, 864),
    (76, 2, 100),
    (72, 27, 8),
    (9, 32, 616),
    (20, 54, 822),
    (28, 58, 813),
    (5, 65, 997),
    (21, 72, 387),
    (67, 36, 4),
    (6, 55, 206),
    (54, 64, 260),
    (3, 16, 45),
    (71, 23, 81),
    (1, 45, 715),
    (41, 42, 291),
    (68, 78, 298),
    (74, 70, 16),
    (78, 55, 242),
    (58, 59, 851),
    (4, 19, 1),
    (27, 22, 618),
    (58, 64, 751),
    (68, 75, 578),
    (29, 24, 69),
    (18, 36, 825),
    (51, 37, 914),
    (77, 39, 776),
    (62, 63, 293),
    (51, 13, 809),
    (79, 63, 227),
    (28, 7, 849),
    (65, 38, 166),
    (62, 74, 520),
    (61, 4, 832),
    (8, 71, 989),
    (12, 67, 239),
    (59, 43, 686),
    (41, 73, 246),
    (4, 42, 842),
    (29, 60, 349),
    (17, 3, 380),
    (15, 68, 927),
    (32, 60, 269),
    (65, 38, 784),
    (19, 5, 641),
]
for x in range(len(edges)):
    g.addEdge(edges[x][0], edges[x][1], edges[x][2])

g.reverseDeleteMST()
fin = time.time()
print(f'tiempo de ejecucion{fin-inicio}')

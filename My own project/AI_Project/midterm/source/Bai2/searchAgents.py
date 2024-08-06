from fringes import PriorityQueue
import math
import copy

# Định nghĩa hàm uniformCostSearch để thực hiện tìm kiếm chi phí đồng nhất.
def uniformCostSearch(problem):
    # Tìm kiếm đường đi từ vị trí bắt đầu đến vị trí thức ăn.
    def search(start_position, food_position):
        visited = set()  # Lưu các vị trí đã thăm.
        statePQ = PriorityQueue()  # Tạo hàng đợi ưu tiên cho các trạng thái.
        statePQ.push((start_position, [], 0), 0)  # Đưa trạng thái ban đầu vào hàng đợi.

        # Lặp cho đến khi hàng đợi rỗng.
        while not statePQ.isEmpty():
            position, path, cost = statePQ.pop()  # Lấy trạng thái có chi phí thấp nhất.

            if position == food_position:  # Kiểm tra nếu đã đến đích.
                return path

            if position in visited:  # Bỏ qua nếu đã thăm.
                continue
            visited.add(position)  # Đánh dấu đã thăm.

            # Lấy các hành động có thể từ vị trí hiện tại.
            actions = problem.agent.get_possible_actions(problem.init_state, position)
            for action in actions:
                new_pos_agent = problem.successor(position, action)  # Tính vị trí mới sau hành động.
                new_path = path + [action]  # Tạo đường đi mới.
                new_cost = cost + 1  # Tính toán chi phí mới.
                statePQ.push((new_pos_agent, new_path, new_cost), new_cost)  # Thêm trạng thái mới vào hàng đợi.
        return []  # Trả về đường đi rỗng nếu không tìm thấy.

    # Lấy vị trí bắt đầu và các mục tiêu (thức ăn và góc).
    start_position = problem.agent.get_pos()
    try: foods = problem.foods
    except: foods = [problem.food]
    try: corners = problem.corners
    except: corners = [problem.corner]

    merged_path = []  # Đường đi tổng hợp từ nhiều mục tiêu.
    # Tạo danh sách vị trí mục tiêu từ thức ăn và góc.
    foods_ = [food.get_pos() for food in copy.deepcopy(foods)]
    foods_.extend(corner.get_pos() for corner in copy.deepcopy(corners))
    
    # Tìm đường đi ngắn nhất đến từng mục tiêu.
    while len(foods_) > 0:
        foodPQ = PriorityQueue()  # Tạo hàng đợi ưu tiên cho các mục tiêu.
        for j, food in enumerate(foods_):    
            path = search(start_position, food)  # Tìm đường đi đến mục tiêu.
            cost = problem.get_cost_path(path)  # Tính chi phí đường đi.
            foodPQ.push((food, j, path), cost)  # Thêm vào hàng đợi.
        food_position, j, path = foodPQ.pop()  # Lấy mục tiêu gần nhất.
        del foods_[j]  # Xóa mục tiêu đã đạt được.
        merged_path.extend(path)  # Kết hợp đường đi với tổng hợp.
        start_position = food_position  # Cập nhật vị trí bắt đầu mới.

    # Kiểm tra xem đã đạt được mục tiêu cuối cùng chưa.
    if problem.is_goal(merged_path): return merged_path
    else: return None  # Trả về None nếu không đạt được mục tiêu.
    
def manhatan_path_cost(position,food_position):
    
    if food_position == None: food_position = position
    mahatan_distance = abs(position[0]-food_position[0]) + abs(position[1]-food_position[1])
    return mahatan_distance


def euclidean_path_cost(position,food_position):
    if food_position == None: food_position = position
    euclidean_distance = (position[0]-food_position[0])**2 + (position[1]-food_position[1])**2
    euclidean_distance = math.sqrt(euclidean_distance)
    return euclidean_distance

  
# Định nghĩa hàm tìm kiếm A* cho một vấn đề cụ thể, với một hàm heuristic mặc định là 'manhatan_path_cost'.
def aStarSearch(problem, fn_heuristic=manhatan_path_cost):
    # Định nghĩa hàm nội bộ 'search' để tìm đường đi từ vị trí bắt đầu đến vị trí thức ăn.
    def search(start_position, food_position):
        open_list = PriorityQueue()  # Tạo một hàng đợi ưu tiên để lưu trữ các nút mở.
        visited_list = []  # Danh sách này dùng để theo dõi các vị trí đã thăm.
        path = []  # Đường đi hiện tại từ vị trí bắt đầu.
        priority = 0  # Ưu tiên ban đầu cho nút.
        open_list.push((start_position, path), priority)  # Thêm vị trí bắt đầu vào hàng đợi ưu tiên.

        # Vòng lặp cho đến khi hàng đợi ưu tiên rỗng.
        while not open_list.isEmpty():
            position, path = open_list.pop()  # Lấy vị trí và đường đi từ nút có ưu tiên cao nhất.

            # Nếu vị trí hiện tại là vị trí thức ăn, trả về đường đi tìm được.
            if position == food_position: 
                return path
            # Bỏ qua vị trí nếu nó đã được thăm.
            if position in visited_list:
                continue
            visited_list.append(position)  # Đánh dấu vị trí đã được thăm.

            # Lấy các hành động có thể thực hiện từ vị trí hiện tại.
            actions = problem.agent.get_possible_actions(problem.init_state, position)
            new_pos_agents = []
            # Duyệt qua từng hành động và tạo các trạng thái mới tương ứng.
            for action in actions:
                new_pos_agent = problem.successor(position, action)
                new_pos_agents.append(new_pos_agent)

            # Duyệt qua từng trạng thái mới và đẩy chúng vào hàng đợi ưu tiên.
            for i, new_pos_agent in enumerate(new_pos_agents):
                new_position = new_pos_agent
                new_path = path + [actions[i]]
                g = problem.get_cost_path(new_path)  # Tính toán chi phí g của đường đi mới.
                heuristicValue = fn_heuristic(position, food_position) + g  # Tính toán giá trị heuristic h và tổng chi phí f = g + h.
                open_list.push((new_position, new_path), heuristicValue)  # Đẩy trạng thái mới và đường đi vào hàng đợi với ưu tiên f.
        return []  # Trả về đường đi rỗng nếu không tìm thấy.

    # Lấy vị trí bắt đầu và các mục tiêu (thức ăn và góc).
    start_position = problem.agent.get_pos()
    try: foods = problem.foods
    except: foods = [problem.food]
    try: corners = problem.corners
    except: corners = [problem.corner]

    merged_path = []  # Đường đi tổng hợp từ nhiều mục tiêu.
    # Tạo danh sách vị trí mục tiêu từ thức ăn và góc.
    foods_ = [food.get_pos() for food in copy.deepcopy(foods)]
    foods_.extend(corner.get_pos() for corner in copy.deepcopy(corners))
    
    # Tìm đường đi ngắn nhất đến từng mục tiêu.
    while len(foods_) > 0:
        foodPQ = PriorityQueue()  # Tạo hàng đợi ưu tiên cho các mục tiêu.
        for j, food in enumerate(foods_):    
            path = search(start_position, food)  # Tìm đường đi đến mục tiêu.
            cost = problem.get_cost_path(path)  # Tính chi phí đường đi.
            foodPQ.push((food, j, path), cost)  # Thêm vào hàng đợi.
        food_position, j, path = foodPQ.pop()  # Lấy mục tiêu gần nhất.
        del foods_[j]  # Xóa mục tiêu đã đạt được.
        merged_path.extend(path)  # Kết hợp đường đi với tổng hợp.
        start_position = food_position  # Cập nhật vị trí bắt đầu mới.

    # Kiểm tra xem đã đạt được mục tiêu cuối cùng chưa.
    if problem.is_goal(merged_path): return merged_path
    else: return None  # Trả về None nếu không đạt được mục tiêu.
ucs = uniformCostSearch
astar = aStarSearch


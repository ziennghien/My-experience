import numpy as np
import cv2
import matplotlib.pyplot as plt

#đọc ảnh cần cân bằng Histogram
img = cv2.imread("man_.jpg", 0) 
def compute_hist(img): 
    #tạo mảng hist có 256 phần tử có giá trị bằng 0, có kiểu dữ liệu là số nguyên không dấu 8 bit 
    hist = np.zeros((256,), np.uint8) 
    #lưu chiều cao và chiều rộng của ảnh vào hai biến h và w
    h, w = img.shape[:2] 
    #Xét duyệt từng pixel trong ảnh
    for i in range(h):
        for j in range(w):
            #lưu tần suất xuất hiện của từng mức sáng vào mảng hist
            hist[img[i][j]] += 1
    return hist
#hàm chuyển đổi cân bằng Histogram
def equal_hist(hist):
    #tạo một mảng tichluy có cùng kích thước với mảng hist có các phần tử bằng 0 
    tichluy = np.zeros_like(hist, np.float64)
    #xét duyệt từng phần tử trong tichluy
    for i in range(len(tichluy)):
        #tính tần số tích lũy của từng i và lưu vào phần tử trong tichluy tương ứng
        tichluy[i] = hist[:i].sum()
    #sử dụng tichluy để cân bằng theo công thức
    new_hist = (tichluy - tichluy.min())/(tichluy.max() - tichluy.min())*255
    new_hist = np.uint8(new_hist)
    return new_hist

def match_hist(img, target_hist):
    # Tính histogram của ảnh đầu vào
    img_hist = compute_hist(img)

    # Tính histogram tích lũy của ảnh đầu vào
    img_cum_hist = np.cumsum(img_hist)

    # Tính histogram tích lũy của ảnh mục tiêu
    target_cum_hist = np.cumsum(target_hist)

    # Tạo ánh xạ từ histogram của ảnh đầu vào sang histogram mục tiêu
    mapping = np.interp(img_cum_hist, target_cum_hist, range(256))

    # Áp dụng ánh xạ lên ảnh đầu vào
    matched_img = np.uint8(mapping[img])

    return matched_img

# Đọc ảnh mẫu
target_img = cv2.imread("man.jpg", 0)

# Tính histogram của ảnh mẫu
target_hist = compute_hist(target_img)

# Áp dụng hàm Matching Histogram
result_img = match_hist(img, target_hist)

# Hiển thị ảnh gốc ảnh mẫu và ảnh kết quả

fig, ax = plt.subplots(2,3, figsize=(30,40)) 
ax[0,0].imshow(img, cmap='gray')
ax[0, 0].set_title('Original')
ax[1,0].hist(img.flatten(), 256, [0,256])


ax[0, 1].imshow(target_img, cmap='gray')
ax[0, 1].set_title('Sample')
ax[1, 1].hist(target_img.flatten(), 256, [0,256])    

ax[0, 2].imshow(result_img, cmap='gray')
ax[0, 2].set_title('Matched')
ax[1, 2].hist(result_img.flatten(), 256, [0,256])    

plt.show()
plt.close()

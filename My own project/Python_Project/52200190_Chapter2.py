import numpy as np
import cv2
import matplotlib.pyplot as plt

#đọc ảnh từ file "man.jpg"
img = cv2.imread("man.jpg", 0) 
#hàm tính tần suất xuất hiện của từng mức ánh sáng
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
    #tạo một mảng cum có cùng kích thước với mảng hist có các phần tử bằng 0 
    cum = np.zeros_like(hist, np.float64)
    #xét duyệt từng phần tử trong cum
    for i in range(len(cum)):
        #tính tần số tích lũy của từng i và lưu vào phần tử trong cum tương ứng
        cum[i] = hist[:i].sum()
    #sử dụng cum để cân bằng theo công thức
    new_hist = (cum - cum.min())/(cum.max() - cum.min())*255
    new_hist = np.uint8(new_hist)
    return new_hist
#tạo biến hist bằng cách gọi hàm compute_hist()
hist = compute_hist(img).ravel()
#tạo biến new_hist bằng cách gọi hàm equal_hist()
new_hist = equal_hist(hist)
#tạo hình vẽ có 4 biểu đồ con và kích thước mỗi biểu đồ là 30x20 inch
fig, ax = plt.subplots(2,2, figsize=(30,20))
#vẽ ảnh trước khi cân bằng ở vị trí (0,0) 
ax[0,0].imshow(img, cmap='gray')
ax[0, 0].set_title('Before')
#vẽ biểu đồ Histogram của ảnh trước khi cân bằng
ax[1,0].hist(img.flatten(), 256, [0,256])

h, w = img.shape[:2]
#xét duyệt từng pixel trong ảnh
for i in range(h):
   for j in range(w):
       #thay thế tần suất xuất hiện của các mức sáng trong ảnh => ảnh sau cân bằng
       img[i,j] = new_hist[img[i,j]]
#vẽ ảnh sau cân bằng ở vị trí (0,1)
ax[0, 1].imshow(img, cmap='gray')
ax[0, 1].set_title('After')
#vẽ biểu đồ Histogram của ảnh sau khi cân bằng
ax[1, 1].hist(img.flatten(), 256, [0,256])    
plt.show()
plt.close()





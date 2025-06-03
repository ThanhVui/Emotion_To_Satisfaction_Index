import gdown
import os

# Định nghĩa thư mục và đường dẫn cho mô hình
model_dir = "./models"
model_path = os.path.join(model_dir, "best_model_resemotenet_80.pth")

# Tạo thư mục nếu chưa tồn tại
os.makedirs(model_dir, exist_ok=True)

# URL tải trực tiếp từ Google Drive
url = "https://drive.google.com/file/d/1V7LWDfv7a1-7RtefTKCU5tKUayyZhyPI/view?usp=sharing"

# Tải mô hình
print("Downloading model from Google Drive...")
gdown.download(url, model_path, quiet=False)
print("Model downloaded successfully.")
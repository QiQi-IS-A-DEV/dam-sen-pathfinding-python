# ĐẦM SEN PATHFINDING — SMARTWAY SENPATH

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5 Canvas](https://img.shields.io/badge/HTML5-Canvas-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=for-the-badge&logo=javascript&logoColor=000)

---

## Giới thiệu

Đần Sen Pathfiding - Smartway Senpath là đồ án môn học Trí Tuệ Nhân Tạo trường đại học Mở TP.HCM nhằm giúp sinh viên hiểu rõ hơn về cách thức hoạt động của các thuật toán giải thuật
Đần Sen Pathfiding là một ứng dụng web trực quan giúp người dùng tìm đường đi ngắn nhất trong công viên Đầm Sen qua bản đồ được số hoá. Dự án gồm hai phần:
- **Frotnend**:  HTML/CSS/JS, sử dụng Canvas API để hiển thị bản đồ, node, edge và highlight đường đi.
- **Backend**: Python Flask, cung cấp API /api/graph, quản lý dữ liệu graph (nodes, edges) từ file graph.json.

---

## Thành viên nhóm

- **Lê Việt Hải Quân** - [Email](mailto:2251052100quan@ou.edu.vn) - [Github](https://github.com/QiQi-OU-IT/)


---

## Công nghệ sử dụng

- **Backend**: Flask (Python)
- **Frontend**: HTML5 Canvas + JavaScript thuần
- **Thuật toán**: A\*, Dijkstra (trong `algorithms.py` / JS)
- **Dữ liệu**: `graph.json` (nút, cạnh, toạ độ, trọng số)

---

## Tính năng nổi bật

- Chọn 2 điểm **A/B** trực tiếp trên bản đồ (click node).
- **Zoom/Pan** mượt trên Canvas.
- Tô vẽ đường đi: hiệu ứng **gradient + glow + mũi tên** theo từng cạnh.
- Hiển thị **tổng chiều dài** và **các bước** (breadcrumb + danh sách).
- Chuyển đổi giữa **A\*** và **Dijkstra**.
- Nút **Random A/B** và **Reset** tiện thử nghiệm.

---

## Cấu trúc dự án

```
dam-sen-pathfinding-python/
├─ app.py # Flask app (chạy dev server)
├─ algorithms.py # Thuật toán A* / Dijkstra / build_graph
├─ graph.json # Dữ liệu đồ thị (nút/cạnh/toạ độ)
│
├─ static/
│ ├─ app.js # Logic tương tác & vẽ (Canvas)
│ ├─ algo.js # Thuật toán phía client (nếu dùng)
│ ├─ graph.js # Lớp Graph (parser graph.json)
│ └─ style.css # Giao diện
│
└─ templates/
└─ index.html # Trang chính
```

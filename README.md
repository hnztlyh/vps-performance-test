# VPS Performance Test

This project is designed to test and log the performance of a VPS.

## Features

- CPU Usage
- Memory Usage
- Disk I/O
- Network Speed (Download & Upload)

The test is executed weekly and results are logged in `performance_log.txt`.

## Setup

1. Clone the repository.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the script manually:
    ```bash
    python vps_performance_test.py
    ```

## 使用指南

### 步骤概览

1. **通过 Git 克隆项目**：从 GitHub 上克隆你上传的性能测试项目。
2. **安装依赖**：确保安装脚本所需的 Python 库。
3. **运行脚本**：执行性能测试并查看结果。
4. **定期运行（可选）**：使用 cron 作业定期自动运行性能测试。

---

###  克隆 GitHub 项目到 VPS

在 VPS 上通过 **FinalShell** 连接后，你可以执行以下命令来 **克隆** 项目：

```bash
# 使用 git 克隆你的 GitHub 仓库到 VPS
git clone https://github.com/hnztlyh/vps-performance-test.git

# 进入项目目录
cd vps-performance-test

# 更新 pip
python3 -m pip install --upgrade pip

# 安装依赖库
pip install -r requirements.txt

# 安装 Python3
sudo apt-get update
sudo apt-get install python3 python3-pip

# 执行性能测试脚本
python3 vps_performance_test.py

# 查看性能日志
cat performance_log.txt

# 编辑 cron 配置
crontab -e

# 添加以下内容（每周日凌晨 12 点执行）
0 0 * * 0 cd /path/to/vps-performance-test && python3 vps_performance_test.py >> /path/to/vps-performance-test/performance_log.txt 2>&1

替换 /path/to/vps-performance-test 为你项目的实际路径。这样，系统会每周自动运行一次性能测试。

🌟 总结：
克隆项目：从 GitHub 克隆项目到 VPS。

安装依赖：安装 psutil 和 speedtest-cli 库。

运行测试：执行脚本并查看测试结果。

定期运行：使用 cron 设置定期自动运行性能测试。

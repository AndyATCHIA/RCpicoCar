
# 🚗 RCpicoCar v1.0

A web-controlled RC car powered by the Raspberry Pi Pico W. This project allows full motor control, Wi-Fi setup via access point, and responsive touch-based navigation through a stylish custom web interface.

---

## 📌 Features

- 🔌 **Wi-Fi Setup Mode** via built-in Access Point
- 🌐 **Application Mode** for web-based control over a local network
- 🎮 Control directions: Forward, Reverse, Left, Right, Brake
- 🌡 Internal temperature monitoring
- 💡 Toggle onboard LED
- ♻️ Web-based reset to reconfigure Wi-Fi
- 📱 Mobile-friendly UI with touch and click support

---

## 🧰 Hardware Requirements

| Component              | Details                            |
|------------------------|------------------------------------|
| Raspberry Pi Pico W    | Microcontroller with Wi-Fi         |
| L298N Motor Driver     | For controlling 2 DC motors        |
| 2x DC Motors           | For movement                       |
| Power Source           | Battery pack for motors and Pico   |
| Jumper Wires, Chassis  | For wiring and body of the car     |

---

## 🔌 Pin Configuration

| Function            | Pico W GPIO |
|---------------------|-------------|
| Motor A Enable      | GP0         |
| Motor A IN1 / IN2   | GP1 / GP2   |
| Motor B IN1 / IN2   | GP3 / GP4   |
| Motor B Enable      | GP5         |
| Onboard LED         | Built-in    |

---

## 🚀 How It Works

### 🔧 Setup Mode (Access Point)

When first powered up (or after reset), the Pico W starts in **Setup Mode**:

1. Creates a Wi-Fi hotspot called `pi pico`.
2. Hostname: `http://pipico.net`
3. Users connect and enter home Wi-Fi credentials.
4. Pico W stores them, reboots, and connects to the network.

### 🌐 Application Mode (Web Control)

Once connected to Wi-Fi:

- The device starts a web server.
- Visit its IP address to control the car in real time.
- Uses `/forward_on`, `/turn_left_on`, etc. for navigation control.

---

## 🖥 Web Interface Overview

### `index.html`

The primary user interface for controlling the car.

**Elements:**

- Title: `R C Army Truck`
- Status message: Connected / Mode
- **Remote Control Grid**:
  - Front, Back, Left, Right, Brake
- **Utility Buttons**:
  - Reset Wi-Fi
  - Change Driving Mode (manual/auto)

**Features:**

- Built-in **JavaScript** handles real-time commands using `navigator.sendBeacon()`
- Responsive design for phones and tablets
- Stylish button layout with CSS hover effects



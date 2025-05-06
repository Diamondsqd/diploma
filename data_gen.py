import pandas as pd
import numpy as np

# Установка случайности для воспроизводимости
np.random.seed(42)

# Параметры генерации
n_samples = 100000
cities = ["Москва", "Санкт-Петербург", "Казань", "Новосибирск", "Екатеринбург"]
cargo_types = ["общий", "скоропортящийся", "опасный", "хрупкий"]
transport_types = ["авто", "жд", "авиа", "морской"]
seasons = ["зима", "весна", "лето", "осень"]
days_of_week = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]

# Генерация данных
data = {
    "origin_city": np.random.choice(cities, n_samples),
    "destination_city": np.random.choice(cities, n_samples),
    "distance_km": np.random.randint(100, 3000, n_samples),
    "weight_tons": np.round(np.random.uniform(0.5, 20.0, n_samples), 2),
    "volume_m3": np.round(np.random.uniform(1.0, 100.0, n_samples), 2),
    "cargo_type": np.random.choice(cargo_types, n_samples),
    "transport_type": np.random.choice(transport_types, n_samples),
    "season": np.random.choice(seasons, n_samples),
    "day_of_week": np.random.choice(days_of_week, n_samples),
    "fuel_price": np.round(np.random.uniform(40, 80, n_samples), 2)
}

# Формула для генерации стоимости
def compute_price(row):
    base_rate = 2.0
    weight_factor = 10.0
    volume_factor = 0.5
    fuel_factor = 1.2

    distance_cost = base_rate * row["distance_km"]
    weight_cost = weight_factor * row["weight_tons"]
    volume_cost = volume_factor * row["volume_m3"]
    fuel_cost = fuel_factor * row["fuel_price"]

    cargo_modifier = {
        "общий": 1.0, "скоропортящийся": 1.2, "опасный": 1.5, "хрупкий": 1.1
    }
    transport_modifier = {
        "авто": 1.0, "жд": 0.9, "авиа": 2.0, "морской": 0.8
    }

    modifier = cargo_modifier[row["cargo_type"]] * transport_modifier[row["transport_type"]]
    return round((distance_cost + weight_cost + volume_cost + fuel_cost) * modifier, 2)

df = pd.DataFrame(data)
df["price_rub"] = df.apply(compute_price, axis=1)

# Сохранение датасета
file_path = "transport_dataset_ml.csv"
df.to_csv(file_path, index=False)

file_path

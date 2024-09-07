from airflow.decorators import dag, task
from datetime import datetime, timedelta
import random

@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    description='A simple DAG to generate and check random numbers',
    catchup=False
)
def random_nbr_checker_taskflow():
    @task()
    def generate_random_nbr_task():
        number = random.randint(1, 100)
        print(f"Generated random number: {number}")
        return number
    
    @task()
    def check_even_odd_task(number):
        result = "even" if number % 2 == 0 else "odd"
        print(f"The number {number} is {result}.")

    number = generate_random_nbr_task()
    check_even_odd_task(number)

random_nbr_checker_taskflow() 
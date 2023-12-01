import requests
import asyncio
import urllib3
import httpx
import os
from dotenv import load_dotenv
from datetime import datetime, timezone


load_dotenv()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = os.environ.get("BASE_URL")



async def add_employees(customer_ids: str, segment_id: str):
    payload  = {
      "customerIds": customer_ids,
      "segmentId": segment_id,
      "operationDate": str(datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%fZ')),
      "interactionChannel": "UserInterface"
    }

    headers = {
        "Content-Type": "application/json",
    }

    url = f"{BASE_URL}/api/static_segments/add_clients_to_segment"
    client = httpx.AsyncClient(verify=False)

    try:
        response = await client.post(url, json=payload, headers=headers, )
    except Exception as e:
        raise Exception("Произошла ошибка сервера при добавлении сотрудников в сегмент.")


    if response.status_code == 200:
        print(response.content)
    else:
        print(f"Error: {response.status_code}")
        print(response.content)
        raise Exception("Не удалось выполнить обновление с кодом состояния 200 (успешно).")




async def remove_employees(customer_ids: str, segment_id: str):
    payload = {
        "customerIds": customer_ids,
        "operationDate": str(datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%fZ')),
        "segmentId": segment_id,
        "interactionChannel": "UserInterface"
    }

    headers = {
        "Content-Type": "application/json",
    }

    url = f"{BASE_URL}/api/static_segments/delete_clients_from_segment"
    client = httpx.AsyncClient(verify=False)
    print(payload)

    try:
        response = await client.post(url, json=payload, headers=headers)
    except Exception:
        raise Exception("Произошла ошибка сервера при удалении сотрудников из сегмента.")

    if response.status_code == 200:
        print(response.content)
    else:
        print(f"Failed: {response.status_code}")
        print(response.content)
        raise Exception("Не удалось выполнить обновление с кодом состояния 200 (успешно).")


async def main():
    # adding = asyncio.create_task(add_employees(segment_id="Employees", customer_ids=['998971551455', '998902766551']))
    deleting = asyncio.create_task(remove_employees(segment_id="Employees", customer_ids=['998971551455', '998902766551']))

    await asyncio.gather(deleting)

if __name__ == "__main__":
    asyncio.run(main())





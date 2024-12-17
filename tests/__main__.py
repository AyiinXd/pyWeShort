from asyncio import run
from sys import argv

from . import client


async def createShortUrl():
    res = await client.createShortUrl("https://youtu.be/YcQFi-1lAOo?si=pZO1WopFBjU2B6XJ", 1000)
    print(res)


async def deleteShortUrl():
    res = await client.deleteShortUrl("tyrqopeb")
    print(res)

# https://weshort.pro/tyrqopeb
async def getShortUrl():
    res = await client.getShortUrl("tyrqopeb")
    print(f"""
Detail Short URL:

Client Name: {res.clientName}
Url: {res.url}
Keyword: {res.keyword}
Price: {res.price}
Views: {res.views}
Payments: {res.payments}
Created At: {res.createdAt}
Updated At: {res.updatedAt}
Short Url: {res.shortUrl}
    """)

async def getShortsUrl():
    res = await client.getShortsUrl()
    for x in res:
        print({
            "Client Name": x.clientName,
            "Url": x.url,
            "Keyword": x.keyword,
            "Price": x.price,
            "Views": x.views,
            "Payments": x.payments,
            "Created At": x.createdAt,
            "Updated At": x.updatedAt,
            "Short Url": x.shortUrl
        })


async def getWithdraws():
    res = await client.getWithdraws()
    for x in res:
        print(f"""
Withdraws:

Client Name: {x.clientName}
Amount: {x.amount}
Status: {x.status}
Fee Admin: {x.feeAdmin}
Created At: {x.createdAt}
Updated At: {x.updatedAt}
        """)

async def getWithdraw():
    res = await client.getWithdraw("withdrawId")
    print(f"""
Withdraws:

Client Name: {res.clientName}
Amount: {res.amount}
Status: {res.status}
Fee Admin: {res.feeAdmin}
Created At: {res.createdAt}
Updated At: {res.updatedAt}
    """)

async def createWithdraw():
    res = await client.requestWithdraws(
        nameRek="AyiinDevs",
        noRek="123456789",
        amount="1000",
        method="Bank SeaBank"
    )
    print(res)

if __name__ == "__main__":
    if len(argv) > 1:
        if argv[1] == "short":
            if len(argv) > 2:
                if argv[2] == "create":
                    run(createShortUrl())
                elif argv[2] == "delete":
                    run(deleteShortUrl())
                elif argv[2] == "get":
                    run(getShortUrl())
                elif argv[2] == "gets":
                    run(getShortsUrl())
        elif argv[1] == "wd":
            if len(argv) > 2:
                if argv[2] == "gets":
                    run(getWithdraws())
                elif argv[2] == "get":
                    run(getWithdraw())
                elif argv[2] == "create":
                    run(createWithdraw())
        else:
            print("Usage: python3 main.py [short|wd] [create|delete|get]")
    else:
        print("Usage: python3 main.py [short|wd] [create|delete|get]")

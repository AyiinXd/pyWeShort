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


async def getPayments():
    res = await client.getPayments()
    for x in res:
        print(f"""
Payments:

Client Name: {x.ownerName}
Order Id: {x.orderId}
Amount: {x.amount}
Status: {x.status}
Created At: {x.createdAt}
Updated At: {x.updatedAt}
        """)


async def getPayment():
    res = await client.getPayment("xxxx1e2e0c3a062b17025exxxx754b5c51597c57445e26495c0f5a770107")
    print(f"""
Payments:

Client Name: {res.ownerName}
Order Id: {res.orderId}
Amount: {res.amount}
Status: {res.status}
Created At: {res.createdAt}
Updated At: {res.updatedAt}
    """)


async def createPayment():
    res = await client.createPayment("https://weshort.pro/tyrqopeb")
    print(f"""
Payment Created

Qris Token: {res.qrisToken}
Transaction Id: {res.transactionId}
Order Id: {res.orderId}
Expired At: {res.expired}
    """)
    path = await client.generateQris(res.qrisToken)
    print(path)


async def checkTransaction():
    res = await client.checkTransaction("xxxx1e2e0c3a062b17025exxxx754b5c51597c57445e26495c0f5a770107")
    # Jika response data tidak kosong
    if res.data:
        print(f"""
Data Payment

Status Code: {res.payment.statusCode}
Amount: {res.payment.amount}
Currency: {res.payment.currency}
Payment Type: {res.payment.paymentType}
Transaction Status: {res.payment.transactionStatus}
Fraud Status: {res.payment.fraudStatus}
Transaction Time: {res.payment.transactionTime}
Expired Time: {res.payment.expiredTime}


Data Transacation:

Keyword: {res.data.keyword}
ShortUrl: {res.data.shortUrl}
OriginUrl: {res.data.url}
        """)
        return

    # Jika response data kosong
    print(f"""
Payment Checked

Status Code: {res.statusCode}
Transaction Id: {res.transactionId}
Order Id: {res.orderId}
Amount: {res.amount}
Currency: {res.currency}
Payment Type: {res.paymentType}
Transaction Status: {res.transactionStatus}
Fraud Status: {res.fraudStatus}
Transaction Time: {res.transactionTime}
Expired Time: {res.expiredTime}
    """)


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
        elif argv[1] == "pay":
            if len(argv) > 2:
                if argv[2] == "gets":
                    run(getPayments())
                elif argv[2] == "get":
                    run(getPayment())
                elif argv[2] == "create":
                    run(createPayment())
                elif argv[2] == "cek":
                    run(checkTransaction())
        else:
            print("Usage: python3 main.py [short|wd|pay] [create|delete|get]")
    else:
        print("Usage: python3 main.py [short|wd|pay] [create|delete|get]")


while 1:
    if contract.receiveData().call()==true:
        address=contract.recieveAddress().call()
        if PORT=="8888":
                contract.send(sender=address[2])
        elif PORT=="8889":
                contract.send(sender=address[3])
        elif PORT=="8890":
                contract.send(sender=address[4])

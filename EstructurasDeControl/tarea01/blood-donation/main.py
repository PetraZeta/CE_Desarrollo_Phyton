def run(age: int, weight: int, heartbeat: int, platelets: int) -> bool:
    suitable_for_donation = True
    if age < 18 or age > 65:
        suitable_for_donation = False
        print("Eres demasiado joven o muy viejo")
    if weight < 50:
        suitable_for_donation = False
        print("Peso demasiado bajo")
    if heartbeat < 50 or heartbeat > 110:
        suitable_for_donation = False
        print("Pulso anormal")
    if platelets < 125000:
        suitable_for_donation = False
        print("No tienes suficientes plaquetas")
    if platelets < 135000 and platelets > 125000:
        print("Puedes donar si eres mujer")
    return suitable_for_donation


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

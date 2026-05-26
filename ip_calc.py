def calculate_ip_details(ip_str, mask_str):
    ip_parts = [int(x) for x in ip_str.split('.')];
    mask_parts = [int(x) for x in mask_str.split('.')];

    network_parts = []
    broadcast_parts = []

    for i in range(4):
        current_ip_octet = ip_parts[i]
        current_mask_octet = mask_parts[i]
        net_octet = current_ip_octet & current_mask_octet
        network_parts.append(str(net_octet))

        invert_mask = 255 - current_mask_octet
        broadcast_octet = net_octet | invert_mask
        broadcast_parts.append(str(broadcast_octet))

    network_id = '.'.join(network_parts)
    broadcast_id = '.'.join(broadcast_parts)
    return network_id, broadcast_id

ip = "192.168.1.50"
mask = "255.255.255.0"

net_id, broadcast_id = calculate_ip_details(ip, mask)
print(f"Network ID: {net_id}")
print(f"Broadcast ID: {broadcast_id}")

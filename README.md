# Campus Network Design – Cisco Packet Tracer

## 1. Project Overview

This project presents the design and simulation of a multi-floor campus network for a Faculty of Information Technology using Cisco Packet Tracer.

The network was designed to provide reliable connectivity between departments while ensuring network segmentation, security, redundancy, and external connectivity.

The implementation includes 15 VLANs, Inter-VLAN Routing, DHCP, HSRP, ACLs, static routing, WAN/cloud connectivity, and an IoT-based Smart Parking system.

## 2. Project Objectives

- Design a scalable hierarchical network architecture across four floors.
- Configure 15 VLANs for traffic segmentation across departments.
- Implement Inter-VLAN Routing for communication between network segments.
- Deploy DHCP services for automatic IP address allocation.
- Implement HSRP for gateway redundancy and failover.
- Apply ACL rules to secure sensitive network segments.
- Configure static routing and WAN/cloud connectivity.
- Integrate an IoT-based Smart Parking system.
- Perform connectivity, redundancy, and security testing.

## 3. Technologies Used

- Cisco Packet Tracer
- VLANs and 802.1Q Trunking
- Inter-VLAN Routing
- DHCP
- HSRP
- Access Control Lists (ACLs)
- Static Routing
- WAN/Cloud Connectivity
- IoT Smart Parking

## 4. Network Architecture
<img width="1467" height="778" alt="image" src="https://github.com/user-attachments/assets/a6ffcc85-cab5-47d8-8dc0-5b606635814d" />

The network consists of:

- Main Router and Backup Router
- Two Core Switches
- Access switches distributed across four floors
- 15 VLANs for departmental and service segmentation
- Dedicated network segments for different departments
- WAN/Cloud connectivity
- IoT devices for the Smart Parking system

## 5. Implementation

### VLAN Configuration
Configured 15 VLANs to separate departmental traffic and improve network segmentation.

### Inter-VLAN Routing
Implemented Inter-VLAN Routing to enable communication between different VLANs.

### DHCP
Deployed DHCP services to automatically assign IP addresses to network devices.

### HSRP
Implemented HSRP to provide gateway redundancy and maintain network availability during router failures.

### Access Control Lists (ACLs)
Configured ACL rules to control traffic and restrict unauthorized access to sensitive network segments.

### Static Routing and WAN Connectivity
Configured static routing and WAN/cloud connectivity to enable communication with external networks.

### IoT Smart Parking
Integrated an IoT-based Smart Parking system using simulated IoT devices within the campus network.

## 6. Verification and Testing

The network was tested to verify connectivity, routing, redundancy, and security.

The following commands were used:

- `show vlan brief`
- `show interfaces trunk`
- `show ip route`
- `show ip dhcp binding`
- `show standby brief`
- `show access-lists`

Testing included:

- Inter-VLAN connectivity verification.
- DHCP address assignment.
- HSRP redundancy and failover testing.
- WAN connectivity verification.
- ACL traffic filtering.
- IoT Smart Parking functionality.

Screenshots and test results are included in the screenshots directory.

## 7. Project Files

- Cisco Packet Tracer simulation file.
- Network topology diagram.
- Router and switch configurations.
- Verification screenshots.
- Project documentation.

## 8. Learning Outcomes

This project strengthened my practical understanding of enterprise campus network design, routing and switching, network segmentation, gateway redundancy, access control, WAN connectivity, and IoT integration.

## Tools

- Cisco Packet Tracer

**Project Status:** Completed

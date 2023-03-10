package main

import (
 "fmt"
 "net"
 "time"
)

func main() {
 ip := "127.0.0.1"
 startPort := 1
 endPort := 1024

    fmt.Printf("Scanning %s from %d to %d\n", ip, startPort, endPort)
	for port := startPort; port <= endPort; port++ {
		address := fmt.Sprintf("%s:%d", ip, port)
		fmt.Printf("Scanning %s\n", address)
		conn, err := net.DialTimeout("tcp", address, time.Millisecond*500)
		if err == nil {
			fmt.Printf("%d open\n", port)
			conn.Close()
		}
	}
}
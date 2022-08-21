# containerization-oppgave

Basic python program that generates a complete weighted graph represented with an adjacency matrix, and proposes a solution for the Traveling Salesman Problem with regards to the generated graph. The proposed solution is optimized with a hill climber algorithm, and a before-after comparison is sent to stdout.

The dockerfile inherits from a minimal official python base image.

Developed on Ubuntu virtual machine.
Tested on Windows10 with Rancher Desktop(dockerd moby).

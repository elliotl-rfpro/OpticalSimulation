import KrakenOS as kos

# Create the optical system
system = kos.OpticalSystem("Lens System")

# Define lenses and gaps based on the .kraken file
system.add_lens(radius=28.491, thickness=4.468, index=1.856)
system.add_gap(4.373)
system.add_lens(radius=-34.964, thickness=4.767, index=1.552)
system.add_gap(1.251)
system.add_lens(radius=24.606, thickness=4.153, index=1.62)
system.add_gap(0.1)
system.add_lens(radius=11.876, thickness=4.502, index=1.7)
system.add_gap(0.0)
system.add_lens(radius=-64.462, thickness=3.051, index=1.777)
system.add_gap(0.935)
system.add_lens(radius=18.405, thickness=2.673, index=1.537)
system.add_gap(1.317)
system.add_lens(radius=-36.268, thickness=2.0, index=1.664)
system.add_gap(0.203)
system.add_gap(0.4)
system.add_gap(1.76)
system.add_gap(0.3)
system.add_gap(0.04)
system.add_gap(0.0)

# Plot the optical system
system.plot()

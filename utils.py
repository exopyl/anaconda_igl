def display_axes(size=5):
    pts = np.array([[0, 0, 0], [size, 0, 0], [0, size, 0], [0, 0, size]])

    p.add_edges(pts, np.array([[0, 1]], dtype=np.int), shading={"line_color": "red"})
    p.add_edges(pts, np.array([[0, 2]], dtype=np.int), shading={"line_color": "green"})
    p.add_edges(pts, np.array([[0, 3]], dtype=np.int), shading={"line_color": "blue"})
    

import math

# Function to calculate trigonometric values
def calculate_trigonometric_values(angle_degrees):
    # Convert angle from degrees to radians
    angle_radians = math.radians(angle_degrees)
    
    # Calculate sine, cosine, and tangent
    sine_value = math.sin(angle_radians)
    cosine_value = math.cos(angle_radians)
    tangent_value = math.tan(angle_radians)
    
    return sine_value, cosine_value, tangent_value

# Input: angle in degrees
angle_degrees = float(input("Enter the angle in degrees: "))

# Calculate trigonometric values
sine_value, cosine_value, tangent_value = calculate_trigonometric_values(angle_degrees)

# Output the results
print(f"Sine({angle_degrees}°) = {sine_value}")
print(f"Cosine({angle_degrees}°) = {cosine_value}")
print(f"Tangent({angle_degrees}°) = {tangent_value}")
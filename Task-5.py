import tkinter as tk

def calculate_score():
    # Get the selected values from the GUI
    AccessVector = av_var.get()
    AccessComplexity = ac_var.get()
    Authentication = au_var.get()
    ConfImpact = c_var.get()
    IntegImpact = i_var.get()
    AvailImpact = a_var.get()
    
    # Calculate the Impact and Exploitability metrics
    Impact = 10.41 * (1 - (1 - ConfImpact) * (1 - IntegImpact) * (1 - AvailImpact))
    Exploitability = 20 * AccessVector * AccessComplexity * Authentication
    
    # Calculate the Base Score using the CVSSv2 formula
    if Impact == 0:
        fImpact = 0
    else:
        fImpact = 1.176
    BaseScore = round((((0.6 * Impact) + (0.4 * Exploitability) - 1.5) * fImpact), 1)
    
    # Update the GUI with the calculated score
    score_label.config(text=f"Base Score: {BaseScore}")


# Create the GUI
root = tk.Tk()
root.title("CVSSv2 Calculator")

# Create the AV selector
av_frame = tk.Frame(root)
av_label = tk.Label(av_frame, text="Access Vector:")
av_label.pack(side=tk.LEFT, padx=5, pady=5)
av_var = tk.DoubleVar()
av_var.set(1.0)
av_radio_low = tk.Radiobutton(av_frame, text="Low", variable=av_var, value=0.395)
av_radio_low.pack(side=tk.LEFT, padx=5, pady=5)
av_radio_med = tk.Radiobutton(av_frame, text="Medium", variable=av_var, value=0.646)
av_radio_med.pack(side=tk.LEFT, padx=5, pady=5)
av_radio_high = tk.Radiobutton(av_frame, text="High", variable=av_var, value=1.0)
av_radio_high.pack(side=tk.LEFT, padx=5, pady=5)
av_frame.pack(fill=tk.X, padx=10, pady=10)

# Create the AC selector
ac_frame = tk.Frame(root)
ac_label = tk.Label(ac_frame, text="Access Complexity:")
ac_label.pack(side=tk.LEFT, padx=5, pady=5)
ac_var = tk.DoubleVar()
ac_var.set(0.35)
ac_radio_low = tk.Radiobutton(ac_frame, text="Low", variable=ac_var, value=0.71)
ac_radio_low.pack(side=tk.LEFT, padx=5, pady=5)
ac_radio_medium = tk.Radiobutton(ac_frame, text="Medium", variable=ac_var, value=0.61)
ac_radio_medium.pack(side=tk.LEFT, padx=5, pady=5)
ac_radio_high = tk.Radiobutton(ac_frame, text="High", variable=ac_var, value=0.35)
ac_radio_high.pack(side=tk.LEFT, padx=5, pady=5)
ac_frame.pack(fill=tk.X, padx=10, pady=10)

# Create the AU selector
au_frame = tk.Frame(root)
au_label = tk.Label(au_frame, text="Authentication:")
au_label.pack(side=tk.LEFT, padx=5, pady=5)
au_var = tk.DoubleVar()
au_var.set(0.704)
au_radio_mult = tk.Radiobutton(au_frame, text="Multiple", variable=au_var, value=0.45)
au_radio_mult.pack(side=tk.LEFT, padx=5, pady=5)
au_radio_single = tk.Radiobutton(au_frame, text="Single", variable=au_var, value=0.56)
au_radio_single.pack(side=tk.LEFT, padx=5, pady=5)
au_radio_none = tk.Radiobutton(au_frame, text="None", variable=au_var, value=0.704)
au_radio_none.pack(side=tk.LEFT, padx=5, pady=5)
au_frame.pack(fill=tk.X, padx=10, pady=10)

# Create the C selector
c_frame = tk.Frame(root)
c_label = tk.Label(c_frame, text="Confidentiality Impact:")
c_label.pack(side=tk.LEFT, padx=5, pady=5)
c_var = tk.DoubleVar()
c_var.set(0.0)
c_radio_none = tk.Radiobutton(c_frame, text="None", variable=c_var, value=0.0)
c_radio_none.pack(side=tk.LEFT, padx=5, pady=5)
c_radio_partial = tk.Radiobutton(c_frame, text="Partial", variable=c_var, value=0.275)
c_radio_partial.pack(side=tk.LEFT, padx=5, pady=5)
c_radio_complete = tk.Radiobutton(c_frame, text="Complete", variable=c_var, value=0.660)
c_radio_complete.pack(side=tk.LEFT, padx=5, pady=5)
c_frame.pack(fill=tk.X, padx=10, pady=10)

# Create the I selector
i_frame = tk.Frame(root)
i_label = tk.Label(i_frame, text="Integrity Impact:")
i_label.pack(side=tk.LEFT, padx=5, pady=5)
i_var = tk.DoubleVar()
i_var.set(0.0)
i_radio_none = tk.Radiobutton(i_frame, text="None", variable=i_var, value=0.0)
i_radio_none.pack(side=tk.LEFT, padx=5, pady=5)
i_radio_partial = tk.Radiobutton(i_frame, text="Partial", variable=i_var, value=0.275)
i_radio_partial.pack(side=tk.LEFT, padx=5, pady=5)
i_radio_complete = tk.Radiobutton(i_frame, text="Complete", variable=i_var, value=0.660)
i_radio_complete.pack(side=tk.LEFT, padx=5, pady=5)
i_frame.pack(fill=tk.X, padx=10, pady=10)

# Create the A selector
a_frame = tk.Frame(root)
a_label = tk.Label(a_frame, text="Availability Impact:")
a_label.pack(side=tk.LEFT, padx=5, pady=5)
a_var = tk.DoubleVar()
a_var.set(0.0)
a_radio_none = tk.Radiobutton(a_frame, text="None", variable=a_var, value=0.0)
a_radio_none.pack(side=tk.LEFT, padx=5, pady=5)
a_radio_partial = tk.Radiobutton(a_frame, text="Partial", variable=a_var, value=0.275)
a_radio_partial.pack(side=tk.LEFT, padx=5, pady=5)
a_radio_complete = tk.Radiobutton(a_frame, text="Complete", variable=a_var, value=0.660)
a_radio_complete.pack(side=tk.LEFT, padx=5, pady=5)
a_frame.pack(fill=tk.X, padx=10, pady=10)

# Create the Calculate button
button_frame = tk.Frame(root)
calculate_button = tk.Button(button_frame, text="Calculate", command=calculate_score)
calculate_button.pack(side=tk.LEFT, padx=5, pady=5)
button_frame.pack(fill=tk.X, padx=10, pady=10)

# Create the score label
score_label = tk.Label(root, text="Base Score: N/A", font=("Helvetica", 16))
score_label.pack(padx=10, pady=10)

def exit_program():
    root.destroy()
# Create the exit button
button_frame = tk.Frame(root)
calculate_button = tk.Button(button_frame, text="Exit", command=exit_program)
calculate_button.pack(side=tk.LEFT, padx=5, pady=5)
button_frame.pack(fill=tk.X, padx=10, pady=10)

# Start the main event loop
root.mainloop()

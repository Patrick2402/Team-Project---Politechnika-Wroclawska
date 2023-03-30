import tkinter as tk
import math

# Create the GUI
root = tk.Tk()
root.title("CVSSv3 Calculator")

# Create the AV selector
av_frame = tk.Frame(root)
av_label = tk.Label(av_frame, text="Attack Vector:")
av_label.pack(side=tk.LEFT, padx=5, pady=5)
av_var = tk.StringVar(value='N')
av_radio_network = tk.Radiobutton(av_frame, text="Network", variable=av_var, value='N')
av_radio_network.pack(side=tk.LEFT, padx=5, pady=5)
av_radio_adjacent = tk.Radiobutton(av_frame, text="Adjacent", variable=av_var, value='A')
av_radio_adjacent.pack(side=tk.LEFT, padx=5, pady=5)
av_radio_local = tk.Radiobutton(av_frame, text="Local", variable=av_var, value='L')
av_radio_local.pack(side=tk.LEFT, padx=5, pady=5)
av_radio_physical = tk.Radiobutton(av_frame, text="Physical", variable=av_var, value='P')
av_radio_physical.pack(side=tk.LEFT, padx=5, pady=5)
av_frame.pack()

# Create the AC selector
ac_frame = tk.Frame(root)
ac_label = tk.Label(ac_frame, text="Attack Complexity:")
ac_label.pack(side=tk.LEFT, padx=5, pady=5)
ac_var = tk.StringVar(value='L')
ac_radio_low = tk.Radiobutton(ac_frame, text="Low", variable=ac_var, value='L')
ac_radio_low.pack(side=tk.LEFT, padx=5, pady=5)
ac_radio_high = tk.Radiobutton(ac_frame, text="High", variable=ac_var, value='H')
ac_radio_high.pack(side=tk.LEFT, padx=5, pady=5)
ac_frame.pack()

# Create the PR selector
pr_frame = tk.Frame(root)
pr_label = tk.Label(pr_frame, text="Privileges Required:")
pr_label.pack(side=tk.LEFT, padx=5, pady=5)
pr_var = tk.StringVar(value='N')
pr_radio_none = tk.Radiobutton(pr_frame, text="None", variable=pr_var, value='N')
pr_radio_none.pack(side=tk.LEFT, padx=5, pady=5)
pr_radio_low = tk.Radiobutton(pr_frame, text="Low", variable=pr_var, value='L')
pr_radio_low.pack(side=tk.LEFT, padx=5, pady=5)
pr_radio_high = tk.Radiobutton(pr_frame, text="High", variable=pr_var, value='H')
pr_radio_high.pack(side=tk.LEFT, padx=5, pady=5)
pr_frame.pack()

# Create the UI selector
ui_frame = tk.Frame(root)
ui_label = tk.Label(ui_frame, text="User Interaction:")
ui_label.pack(side=tk.LEFT, padx=5, pady=5)
ui_var = tk.StringVar(value='N')
ui_radio_none = tk.Radiobutton(ui_frame, text="None", variable=ui_var, value='N')
ui_radio_none.pack(side=tk.LEFT, padx=5, pady=5)
ui_radio_required = tk.Radiobutton(ui_frame, text="Required", variable=ui_var, value='R')
ui_radio_required.pack(side=tk.LEFT, padx=5, pady=5)
ui_frame.pack()

# Create the S selector
s_frame = tk.Frame(root)
s_label= tk.Label(s_frame, text="Scope:")
s_label.pack(side=tk.LEFT, padx=5, pady=5)
s_var = tk.StringVar(value='U')
s_radio_unchanged = tk.Radiobutton(s_frame, text="Unchanged", variable=s_var, value='U')
s_radio_unchanged.pack(side=tk.LEFT, padx=5, pady=5)
s_radio_changed = tk.Radiobutton(s_frame, text="Changed", variable=s_var, value='C')
s_radio_changed.pack(side=tk.LEFT, padx=5, pady=5)
s_frame.pack()

#Create the CI selector
ci_frame = tk.Frame(root)
ci_label = tk.Label(ci_frame, text="Confidentiality Impact:")
ci_label.pack(side=tk.LEFT, padx=5, pady=5)
ci_var = tk.StringVar(value='N')
ci_radio_none = tk.Radiobutton(ci_frame, text="None", variable=ci_var, value='N')
ci_radio_none.pack(side=tk.LEFT, padx=5, pady=5)
ci_radio_low = tk.Radiobutton(ci_frame, text="Low", variable=ci_var, value='L')
ci_radio_low.pack(side=tk.LEFT, padx=5, pady=5)
ci_radio_high = tk.Radiobutton(ci_frame, text="High", variable=ci_var, value='H')
ci_radio_high.pack(side=tk.LEFT, padx=5, pady=5)
ci_frame.pack()

#Create the II selector
ii_frame = tk.Frame(root)
ii_label = tk.Label(ii_frame, text="Integrity Impact:")
ii_label.pack(side=tk.LEFT, padx=5, pady=5)
ii_var = tk.StringVar(value='N')
ii_radio_none = tk.Radiobutton(ii_frame, text="None", variable=ii_var, value='N')
ii_radio_none.pack(side=tk.LEFT, padx=5, pady=5)
ii_radio_low = tk.Radiobutton(ii_frame, text="Low", variable=ii_var, value='L')
ii_radio_low.pack(side=tk.LEFT, padx=5, pady=5)
ii_radio_high = tk.Radiobutton(ii_frame, text="High", variable=ii_var, value='H')
ii_radio_high.pack(side=tk.LEFT, padx=5, pady=5)
ii_frame.pack()

#Create the AI selector
ai_frame = tk.Frame(root)
ai_label = tk.Label(ai_frame, text="Availability Impact:")
ai_label.pack(side=tk.LEFT, padx=5, pady=5)
ai_var = tk.StringVar(value='N')
ai_radio_none = tk.Radiobutton(ai_frame, text="None", variable=ai_var, value='N')
ai_radio_none.pack(side=tk.LEFT, padx=5, pady=5)
ai_radio_low = tk.Radiobutton(ai_frame, text="Low", variable=ai_var, value='L')
ai_radio_low.pack(side=tk.LEFT, padx=5, pady=5)
ai_radio_high = tk.Radiobutton(ai_frame, text="High", variable=ai_var, value='H')
ai_radio_high.pack(side=tk.LEFT, padx=5, pady=5)
ai_frame.pack()

#Create the Calculate button
calculate_button = tk.Button(root, text="Calculate", command=lambda: calculate_cvss())
calculate_button.pack(pady=10)

# Create the score label
score_label = tk.Label(root, text="Base Score: N/A", font=("Helvetica", 16))
score_label.pack(padx=10, pady=10)

#Function to calculate the CVSS score
def calculate_cvss():
    av = av_var.get()
    ac = ac_var.get()
    pr = pr_var.get()
    ui = ui_var.get()
    s = s_var.get()
    ci = ci_var.get()
    ii = ii_var.get()
    ai = ai_var.get()


    # Convert selected values to their corresponding scores
    s_score = {'U': 0, 'C': 1}[s]

    av_score = {'N': 0.85, 'A': 0.62, 'L': 0.55, 'P': 0.2}[av]
    ac_score = {'H': 0.44, 'L': 0.77}[ac]
    if s_score==0:
        pr_score = {'N': 0.85, 'L': 0.62, 'H': 0.27}[pr]
    if s_score==1:
        pr_score = {'N': 0.85, 'L': 0.68, 'H': 0.5}[pr]
    ui_score = {'N': 0.85, 'R': 0.62}[ui]
    ci_score = {'N': 0, 'L': 0.22, 'H': 0.56}[ci]
    ii_score = {'N': 0, 'L': 0.22, 'H': 0.56}[ii]
    ai_score = {'N': 0, 'L': 0.22, 'H': 0.56}[ai]

    ISS=1 - ( (1 - ci_score) * (1 - ii_score) * (1 - ai_score) )


    if s_score==0:
        Impact=6.42*ISS
    else:
        Impact=7.52 * (ISS - 0.029) - 3.25 * pow(ISS - 0.02,15)

    Exploitability = 8.22 * av_score * ac_score * pr_score * ui_score

    if Impact<=0.0:
        BaseScore=0
    elif s_score==0:
        BaseScore=math.ceil(10*min(Impact+Exploitability,10))/10
    else:
        BaseScore=math.ceil(10*min(1.08*(Impact+Exploitability),10))/10
    score_label.config(text=f"Base Score: {BaseScore}")

def exit_program():
    root.destroy()
# Create the exit button
button_frame = tk.Frame(root)
calculate_button = tk.Button(button_frame, text="Exit", command=exit_program)
calculate_button.pack(side=tk.LEFT, padx=5, pady=5)
button_frame.pack(fill=tk.X, padx=10, pady=10)

# Start the main event loop
root.mainloop()
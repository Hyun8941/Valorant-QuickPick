import customtkinter
import pyautogui as pgi
import time
import threading

pgi.useImageNotFoundException()

app = customtkinter.CTk()
app.title("Hyun's Valorant QuickPick")
app.geometry("300x500")
app.grid_columnconfigure(0, weight=1)

my_font = customtkinter.CTkFont(family="LINE Seed Sans KR Regular", size=14)

# Make the window always on top
app.attributes('-topmost', 1)
# Disable resizing (width and height)
app.resizable(width=False, height=False)

customtkinter.set_widget_scaling(1.2)  # widget dimensions and text size
customtkinter.set_window_scaling(1.2)  # window geometry dimensions

selected_agent = customtkinter.StringVar(value="None")
run_switch_var = customtkinter.StringVar(value="off")

tabview = customtkinter.CTkTabview(master=app)
tabview.grid(row=0, column=0, padx=10, pady=10)

Duelist_tab = tabview.add("Duelist")
Initiator_tab = tabview.add("Initiator")
Sentinel_tab = tabview.add("Sentinel")
Controller_tab = tabview.add("Controller")
tabview.set("Duelist")  # set currently visible tab

#타격대
Jett_radio_b = customtkinter.CTkRadioButton(Duelist_tab, text="제트", variable=selected_agent, value="Jett", font=my_font)
Jett_radio_b.grid(row=2, column=0, padx=10, pady=(10, 10))

Raze_radio_b = customtkinter.CTkRadioButton(Duelist_tab, text="레이즈", variable=selected_agent, value="Raze", font=my_font)
Raze_radio_b.grid(row=3, column=0, padx=10, pady=(10, 10))

Phoenix_radio_b = customtkinter.CTkRadioButton(Duelist_tab, text="피닉스", variable=selected_agent, value="Phoenix", font=my_font)
Phoenix_radio_b.grid(row=4, column=0, padx=10, pady=(10, 10))

Reyna_radio_b = customtkinter.CTkRadioButton(Duelist_tab, text="레이나", variable=selected_agent, value="Reyna", font=my_font)
Reyna_radio_b.grid(row=5, column=0, padx=10, pady=(10, 10))

Yoru_radio_b = customtkinter.CTkRadioButton(Duelist_tab, text="요루", variable=selected_agent, value="Yoru", font=my_font)
Yoru_radio_b.grid(row=6, column=0, padx=10, pady=(10, 10))

Neon_radio_b = customtkinter.CTkRadioButton(Duelist_tab, text="네온", variable=selected_agent, value="Neon", font=my_font)
Neon_radio_b.grid(row=7, column=0, padx=10, pady=(10, 10))

Iso_radio_b = customtkinter.CTkRadioButton(Duelist_tab, text="아이소", variable=selected_agent, value="Iso", font=my_font)
Iso_radio_b.grid(row=8, column=0, padx=10, pady=(10, 10))

#척후대
Gekko_radio_b = customtkinter.CTkRadioButton(Initiator_tab, text="게코", variable=selected_agent, value="Gekko", font=my_font)
Gekko_radio_b.grid(row=2, column=0, padx=10, pady=(10, 10))

Breach_radio_b = customtkinter.CTkRadioButton(Initiator_tab, text="브리치", variable=selected_agent, value="Breach", font=my_font)
Breach_radio_b.grid(row=3, column=0, padx=10, pady=(10, 10))

Sova_radio_b = customtkinter.CTkRadioButton(Initiator_tab, text="소바", variable=selected_agent, value="Sova", font=my_font)
Sova_radio_b.grid(row=4, column=0, padx=10, pady=(10, 10))

Skye_radio_b = customtkinter.CTkRadioButton(Initiator_tab, text="스카이", variable=selected_agent, value="Skye", font=my_font)
Skye_radio_b.grid(row=5, column=0, padx=10, pady=(10, 10))

Kayo_radio_b = customtkinter.CTkRadioButton(Initiator_tab, text="케이오", variable=selected_agent, value="Kayo", font=my_font)
Kayo_radio_b.grid(row=6, column=0, padx=10, pady=(10, 10))

Fade_radio_b = customtkinter.CTkRadioButton(Initiator_tab, text="페이드", variable=selected_agent, value="Fade", font=my_font)
Fade_radio_b.grid(row=7, column=0, padx=10, pady=(10, 10))

#감시자
Deadlock_radio_b = customtkinter.CTkRadioButton(Sentinel_tab, text="데드록", variable=selected_agent, value="Deadlock", font=my_font)
Deadlock_radio_b.grid(row=2, column=0, padx=10, pady=(10, 10))

Sage_radio_b = customtkinter.CTkRadioButton(Sentinel_tab, text="세이지", variable=selected_agent, value="Sage", font=my_font)
Sage_radio_b.grid(row=3, column=0, padx=10, pady=(10, 10))

Cypher_radio_b = customtkinter.CTkRadioButton(Sentinel_tab, text="사이퍼", variable=selected_agent, value="Cypher", font=my_font)
Cypher_radio_b.grid(row=4, column=0, padx=10, pady=(10, 10))

Killjoy_radio_b = customtkinter.CTkRadioButton(Sentinel_tab, text="킬조이", variable=selected_agent, value="Killjoy", font=my_font)
Killjoy_radio_b.grid(row=5, column=0, padx=10, pady=(10, 10))

Chamber_radio_b = customtkinter.CTkRadioButton(Sentinel_tab, text="체임버", variable=selected_agent, value="Chamber", font=my_font)
Chamber_radio_b.grid(row=6, column=0, padx=10, pady=(10, 10))

#전략가
Brimstone_radio_b = customtkinter.CTkRadioButton(Controller_tab, text="브림스톤", variable=selected_agent, value="Brimstone", font=my_font)
Brimstone_radio_b.grid(row=2, column=0, padx=10, pady=(10, 10))

Omen_radio_b = customtkinter.CTkRadioButton(Controller_tab, text="오멘", variable=selected_agent, value="Omen", font=my_font)
Omen_radio_b.grid(row=3, column=0, padx=10, pady=(10, 10))

Viper_radio_b = customtkinter.CTkRadioButton(Controller_tab, text="바이퍼", variable=selected_agent, value="Viper", font=my_font)
Viper_radio_b.grid(row=4, column=0, padx=10, pady=(10, 10))

Astra_radio_b = customtkinter.CTkRadioButton(Controller_tab, text="아스트라", variable=selected_agent, value="Astra", font=my_font)
Astra_radio_b.grid(row=5, column=0, padx=10, pady=(10, 10))

Harbor_radio_b = customtkinter.CTkRadioButton(Controller_tab, text="하버", variable=selected_agent, value="Harbor", font=my_font)
Harbor_radio_b.grid(row=6, column=0, padx=10, pady=(10, 10))

SliderValue = 0.7

def slider_event(value):
    global SliderValue
    print(value)
    SliderValue = float(value)
    print(SliderValue)

confidence_label = customtkinter.CTkLabel(app, text="이미지 서칭 정확도", font=my_font)
confidence_label.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="nsew")

confidence_slider = customtkinter.CTkSlider(app, from_=0, to=1, command=slider_event)
confidence_slider.set(0.7)  # 기본값 설정
confidence_slider.grid(row=2, column=0, padx=10, pady=(10, 10))

def switch_event():
    print("Switch toggled, current value:", run_switch_var.get())
    if run_switch_var.get() == "on":
        execute_script_thread()

def execute_script():
    agent_name = selected_agent.get()

    # Check if agent is selected
    if agent_name == "None":
        print("Error: No agent selected.")
        return

    Agent = Agent = f"Images/{agent_name}.png"

    def find_agent_image():
        try:
            agent_image_location = pgi.locateCenterOnScreen(Agent, confidence=SliderValue)
            return agent_image_location
        except pgi.ImageNotFoundException:
            return None

    def find_lock_in_image():
        try:
            lock_in_image_location = pgi.locateCenterOnScreen("Images/LockIn.png",confidence=SliderValue)
            return lock_in_image_location
        except pgi.ImageNotFoundException:
            return None

    while run_switch_var.get() == "on":
        Agent_image_location = find_agent_image()
        if Agent_image_location:
            print("Agent Image Found at:", Agent_image_location)
            pgi.click(Agent_image_location)
            time.sleep(.1)
            LockIn_image_location = find_lock_in_image()
            if LockIn_image_location:
                print("LockIn Image Found at:", LockIn_image_location)
                pgi.moveTo(LockIn_image_location, duration=0.1)
                pgi.click()
                print("Script Ended")
                break
        else:
            print("Image Not Found")

def execute_script_thread():
    thread = threading.Thread(target=execute_script)
    thread.start()

switch = customtkinter.CTkSwitch(app, text="RUN", command=switch_event, variable=run_switch_var, onvalue="on", offvalue="off", font=my_font)
switch.grid(row=3, column=0, padx=10, pady=(10, 10), sticky="n")

app.mainloop()
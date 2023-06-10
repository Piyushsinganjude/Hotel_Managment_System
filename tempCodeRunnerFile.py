 combo_RoomNo=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("times new roman",12,"bold"),width=8,state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1,sticky=W)
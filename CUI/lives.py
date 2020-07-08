import random
class life:
    manual_mode = "manual"
    auto_mode = "auto"
    def __init__(self, x, y, mode):
        # 自己の配列上の座標
        self.place = (x, y)
        
        # 初期のlifeのstatus
        # 手動：pass
        # 自動：擬似乱数で各life生成時に設定
        if self.manual_mode == mode:
            pass
            
        elif self.auto_mode == mode:
            self.current_status = random.randint(0, 1)
        
        # 次のlifeのstatus
        self.next_status = 0

    def tell_status(self):
        return self.current_status
    
    def tell_place(self):
        return self.place
    
    # aroud_sumの結果を受けてnext_statusを決める
    def change_status(self, around_sum):
        result = 0
        reason = ""
        if around_sum == 0 or around_sum == 1 or around_sum >=4:
            result = 0
            reason = "過疎か過密"
        elif around_sum == 2:
            result = self.current_status
            reason = "生存"
            
        elif around_sum == 3:
            result = 1
            reason = "誕生"
            
        self.next_status = result
        return (result, reason)
    
    def my_life_tick(self):
        self.current_status = self.next_status
        
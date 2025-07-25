import torch
import torch.nn as nn

class PolicySaver:
    def __init__(self, guide_network: nn.Module, action_policy_network: nn.Module, value_network: nn.Module):
        self.guide_network = guide_network
        self.action_policy_network = action_policy_network
        self.value_network = value_network

    def save_policy_models(self, blueprint_path="blueprint_policy.pth", action_path="baie_action_policy.pth", value_path="baie_value_policy.pth"):
        try:
            torch.save(self.guide_network.state_dict(), blueprint_path)
            print(f"\n\033[92m引导网络模型已成功导出至: {blueprint_path}\033[0m")
            torch.save(self.action_policy_network.state_dict(), action_path)
            print(f"\n\033[92m卡厄斯兰那行动策略模型已成功导出至: {action_path}\033[0m")
            torch.save(self.value_network.state_dict(), value_path)
            print(f"\033[92m卡厄斯兰那价值评估模型已成功导出至: {value_path}\033[0m")
        except Exception as e:
            print(f"\n\033[91m错误: 无法保存策略模型。原因: {e}\033[0m")

class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        met_target = []
        for employee in hours:
            if employee >= target:
                met_target.append(employee)
        return len(met_target)
def replace_in_xml_file(
        file_path,
        target_strings,  # 第一类：触发 Integer/int 替换的关键词
        map_keywords,  # 第二类：触发整行替换为 map 模板的关键词
        output_path=None
):
    """
    处理XML文件，支持两类规则：
      1. 类型替换：含 target_strings 且含 Integer/int → 替换类型
      2. 结构替换：含 map_keywords → 整行替换为 map 模板（优先级更高）

    :param file_path: 输入文件路径
    :param target_strings: 触发类型替换的关键词列表（子串匹配）
    :param map_keywords: 触发结构替换的关键词列表（子串匹配）
    :param output_path: 输出路径
    """
    # 初始化第一类统计
    type_replace_count = {s: 0 for s in target_strings}
    total_type_modified = 0

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    modified_lines = []
    before_modify_lines = []

    for line in lines:
        # ===== 第二类：结构替换（高优先级）=====
        matched_map_keyword = None
        for kw in map_keywords:
            if kw in line:
                matched_map_keyword = kw
                break  # 取第一个匹配的即可（或你可改为收集所有，但模板只需一个）

        if matched_map_keyword:
            # 生成模板（注意缩进和格式）
            template = (
                f'<map1 alias="{matched_map_keyword}" field="{matched_map_keyword}" '
                f'javaType="java.util.Map" required="false" bizKeyFlag="false">\n'
                f'  <mapType>\n'
                f'    <string fieldLength="32" alias="value" field="value" '
                f'javaType="java.lang.String" demo="value" required="false" bizKeyFlag="false" />\n'
                f'  </mapType>\n'
                f'</map1>\n'
            )
            modified_lines.append(template)
            before_modify_lines.append(line)
            continue  # 跳过第一类处理

        # ===== 第一类：类型替换（低优先级）=====
        has_integer = 'Integer' in line
        has_int = 'int' in line
        if not (has_integer or has_int):
            modified_lines.append(line)
            continue

        matched_targets = [word for word in target_strings if word in line]
        if matched_targets:
            new_line = line.replace('Integer', 'Long').replace('int', 'long')
            before_modify_lines.append(line)
            modified_lines.append(new_line)
            total_type_modified += 1
            for word in matched_targets:
                type_replace_count[word] += 1
        else:
            modified_lines.append(line)

    # ===== 输出结果 =====
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(modified_lines)
        print(f"✅ 处理完成，结果已保存至：{output_path}")
    else:
        print("".join(modified_lines))

    # ===== 输出统计 =====
    print("\n📊 第一类：真实类型替换行数统计（仅含实际替换的行）：")
    for word in target_strings:
        print(f'  "{word}" → {type_replace_count[word]} 行')
    print(f"\n📝 第一类总共修改了 {total_type_modified} 行")

    # 修改前的文本行
    print(f"\n🔄 修改的文本行：")
    for line in before_modify_lines:
        print(str.lstrip(line))


# ===== 使用示例 =====
if __name__ == "__main__":
    input_file = "C:\\Users\\admin\\Desktop\\新文件2.xml"  # 输入文件
    target_strings = ["field=\"divisionId\"", "field=\"countryId\"", "field=\"provinceId\"", "field=\"cityId\"",
                      "field=\"districtId\"", "field=\"townId\"", ]  # 多个匹配字符串（区分大小写）
    map_keywords = ["featureMap", "feature"]  # 第二类关键词
    output_file = "output.xml"  # 输出文件（设为 None 可打印到控制台）

    replace_in_xml_file(input_file, target_strings, map_keywords, output_file)
